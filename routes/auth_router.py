# routes/auth_router.py
from fastapi import APIRouter, HTTPException, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from google.oauth2 import id_token
from google.auth.transport import requests
import os
from fastapi import APIRouter, HTTPException, Request, status, Depends
from dotenv import load_dotenv
import jwt

load_dotenv()

router = APIRouter()
security = HTTPBearer()


@router.post("/login")
async def login(request: Request):
    """Handles Google OAuth authentication and returns a JWT token"""
    try:
        # Get token from Authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(
                status_code=401, detail="Invalid authorization header")

        token_id = auth_header[7:]  # Remove "Bearer " prefix

        # Verify Google token
        client_id = os.getenv("GOOGLE_CLIENT_ID")
        client_secret = os.getenv("GOOGLE_CLIENT_SECRET")

        # Create a Request object for the Google Auth library
        google_request = requests.Request()

        # Verify token with Google
        payload = id_token.verify_oauth2_token(
            token_id, google_request, client_id
        )

        # Check audience
        if payload["aud"] != client_id:
            raise HTTPException(status_code=401, detail="Unauthorized")

        # Extract user info
        email = payload["email"]
        name = payload["name"]

        # Generate JWT token
        secret = os.getenv("SECRET")
        auth_token = jwt.encode(
            {"email": email, "name": name}, secret, algorithm="HS256")

        # Return token in the same format as Express
        return {"authToken": auth_token}

    except Exception as e:
        print(f"Login error: {e}")
        raise HTTPException(status_code=401, detail="Authentication failed")


@router.post("/access")
async def access(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verifies if the user has access"""
    try:
        token = credentials.credentials
        secret = os.getenv("SECRET")

        # Verify JWT token
        decoded = jwt.decode(token, secret, algorithms=["HS256"])

        return {"data": "Authorised"}
    except Exception as e:
        print(f"Access error: {e}")
        return {"data": "NOT Authorised"}
