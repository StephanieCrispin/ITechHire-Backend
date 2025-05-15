# routes/auth_router.py
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from google.oauth2 import id_token
from google.auth.transport import requests
import os
from dotenv import load_dotenv
import jwt
from models.talent import Talent
from models.company import Company
from services.talent_services import TalentServices
from services.company_services import CompanyServices
from utils.jwt_service import create_access_token
load_dotenv()

router = APIRouter()
security = HTTPBearer()


# @router.post("/login")
# async def login(request: Request):
#     """Handles Google OAuth authentication and returns a JWT token"""
#     try:
#         # Get token from Authorization header
#         auth_header = request.headers.get("Authorization")
#         if not auth_header or not auth_header.startswith("Bearer "):
#             raise HTTPException(
#                 status_code=401, detail="Invalid authorization header")

#         token_id = auth_header[7:]  # Remove "Bearer " prefix

#         # Verify Google token
#         client_id = os.getenv("GOOGLE_CLIENT_ID")
#         client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
#         print(f"Client ID: {client_id}")
#         print(f"Client Secret: {client_secret}")

#         # Create a Request object for the Google Auth library
#         google_request = requests.Request()

#         # Verify token with Google
#         payload = id_token.verify_oauth2_token(
#             token_id, google_request, client_id
#         )

#         # Check audience
#         if payload["aud"] != client_id:
#             raise HTTPException(status_code=401, detail="Unauthorized")

#         # Extract user info
#         email = payload["email"]
#         name = payload["name"]

#         # Generate JWT token
#         secret = os.getenv("SECRET")
#         auth_token = jwt.encode(
#             {"email": email, "name": name}, secret, algorithm="HS256")

#         # Return token in the same format as Express
#         return {"authToken": auth_token}

#     except Exception as e:
#         print(f"Login error: {e}")
#         raise HTTPException(status_code=401, detail="Authentication failed")

@router.post("/login")
async def login(request: Request):
    """Handles Google OAuth authentication and returns a JWT token"""
    try:
        body = await request.json()
        user_type = body.get("userType", "talent")
        print(user_type)
        # Get token from Authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(
                status_code=401, detail="Invalid authorization header")

        token_id = auth_header[7:]  # Remove "Bearer " prefix

        # Verify Google token
        client_id = os.getenv("GOOGLE_CLIENT_ID")
        if not client_id:
            raise HTTPException(
                status_code=500, detail="Missing GOOGLE_CLIENT_ID environment variable")

        secret = os.getenv("SECRET")
        if not secret:
            raise HTTPException(
                status_code=500, detail="Missing SECRET environment variable")

        # Create a Request object for the Google Auth library
        google_request = requests.Request()

        # Verify token with Google
        try:
            payload = id_token.verify_oauth2_token(
                token_id, google_request, client_id
            )
        except Exception as verification_error:
            print(f"Token verification error: {verification_error}")
            raise HTTPException(
                status_code=401,
                detail=f"Token verification failed: {str(verification_error)}"
            )

        # Check audience
        if payload["aud"] != client_id:
            raise HTTPException(
                status_code=401, detail="Unauthorized - audience mismatch")

        # Extract user info from Google token
        email = payload["email"]
        name = payload["name"]
        picture = payload["picture"]

        # Split the name into first and last name
        name_parts = name.split(" ", 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ""

        # # Look up or create talent record
        # talent = TalentServices.get_talent_by_email(email)

        # if not talent:
        #     # Talent doesn't exist, create a new one
        #     new_talent = Talent(
        #         first_name=first_name,
        #         last_name=last_name,
        #         email=email,
        #         # No password needed for Google OAuth
        #         # But we might want to set a placeholder or random password
        #         password=None,
        #         oauth_login=True

        #     )

        #     try:
        #         new_talent.save()
        #         talent = new_talent
        #     except Exception as db_error:
        #         print(f"Error creating talent: {db_error}")
        #         raise HTTPException(
        #             status_code=500,
        #             detail="Failed to create talent record"
        #         )

        # # Get talent data for JWT
        # talent_data = talent.to_dict()

        # Check if user_type is company or talent and handle accordingly
        if user_type == "company":
            # Look up or create company record
            company = CompanyServices.get_company_by_email(email)

            if not company:
                # Company doesn't exist, create a new one
                new_company = Company(
                    name=name,
                    email=email,
                    logo=picture,
                    password=None,  # No password needed for Google OAuth
                    oauth_login=True
                )

                try:
                    new_company.save()
                    company = new_company
                except Exception as db_error:
                    print(f"Error creating company: {db_error}")
                    raise HTTPException(
                        status_code=500,
                        detail="Failed to create company record"
                    )

            # Get company data for JWT
            # user_data = company.to_dict()
            # user_role = "company"

        else:  # Default to talent
            # Look up or create talent record (your existing code)
            talent = TalentServices.get_talent_by_email(email)

            if not talent:
                # Talent doesn't exist, create a new one
                new_talent = Talent(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    # No password needed for Google OAuth
                    password=None,
                    oauth_login=True
                )

                try:
                    new_talent.save()
                    talent = new_talent
                except Exception as db_error:
                    print(f"Error creating talent: {db_error}")
                    raise HTTPException(
                        status_code=500,
                        detail="Failed to create talent record"
                    )

            # Get talent data for JWT
            # user_data = talent.to_dict()

        auth_token = create_access_token(
            data={"id": company.to_dict()["_id"],
                  "email": company.to_dict()["email"]})
        print(auth_token)
        return {"authToken": auth_token}

    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        print(f"Login error: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=500, detail=f"Authentication failed: {str(e)}")


# @router.post("/access")
# async def access(credentials: HTTPAuthorizationCredentials = Depends(security)):
#     """Verifies if the user has access"""
#     try:
#         token = credentials.credentials
#         secret = os.getenv("SECRET")

#         # Verify JWT token
#         decoded = jwt.decode(token, secret, algorithms=["HS256"])

#         return {"data": "Authorised"}
#     except Exception as e:
#         print(f"Access error: {e}")
#         return {"data": "NOT Authorised"}
