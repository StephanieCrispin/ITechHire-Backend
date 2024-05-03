# TODO - will need json in the future

# import json
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.talent import Talent
from utils.hashing import Hash
from routes.dto.talent import (
    TalentRequest, LoginTalentRequest, UpdateTalentEmail, UpdateTalentPassword)
from services.talent_services import TalentServices
from utils.jwt_service import create_access_token, verify_token
router = APIRouter()
security = HTTPBearer()


@router.post("/create", status_code=201)
async def create_talent(body: TalentRequest):
    """Create a new document in the talent database"""

    body.password = Hash.hash_password(body.password)
    talent = Talent(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        password=body.password
    )
    try:
        talent.save()
    except Exception as e:
        print(e)
        talent.delete()

        raise HTTPException(
            status_code=500, detail="Email already exists"
        ) from e

    return talent.to_dict()


@router.post("/login")
async def login_talent(body: LoginTalentRequest):

    talent = TalentServices.get_talent_by_email(body.email)

    if not talent:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not Hash.verify_password(body.password, talent.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    print(talent.to_dict())
    access_token = create_access_token(
        data={"id": talent.to_dict()["_id"],
              "email": talent.to_dict()["email"]})
    return {
        "user": talent.to_dict(),
        "access_token": access_token
    }


@router.put("/update-email")
async def update_email(body: UpdateTalentEmail, credentials:
                       HTTPAuthorizationCredentials = Depends(security)):
    """Updates a person's email"""
    token = credentials.credentials
    payload = verify_token(token)
    print(payload["id"])

    talent = TalentServices.get_talent_by_id(payload['id'])

    if not Hash.verify_password(body.password, talent.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    talent.email = body.new_email

    talent.save()

    return talent.to_dict()


@router.put("/update_password")
async def update_password(body: UpdateTalentPassword, credentials:
                          HTTPAuthorizationCredentials = Depends(security)):
    """Updates a person's password"""
    token = credentials.credentials
    payload = verify_token(token)
    talent = TalentServices.get_talent_by_id(payload['id'])

    if not Hash.verify_password(body.old_password, talent.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    body.new_password = Hash.hash_password(
        body.new_password).decode('utf-8').strip()

    talent.password = body.new_password

    talent.save()

    return talent.to_dict()
