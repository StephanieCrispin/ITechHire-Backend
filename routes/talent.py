# TODO - will need json in the future

# import json
from fastapi import APIRouter, HTTPException, status
from models.talent import Talent
from utils.hashing import Hash
from routes.dto.talent import (TalentRequest, LoginTalentRequest)
from services.talent_services import TalentServices
from utils.jwt_service import create_access_token
router = APIRouter()


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
