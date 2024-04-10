from fastapi import FastAPI, HTTPException, Request, status, APIRouter, Path, Depends
from models.user import User
from models.mentor import UpdateMentor
from config.database import users_collection
from schemas.user_serializer import list_serial, individual_serial
from bson.objectid import ObjectId
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
security = HTTPBearer()

router = APIRouter(prefix="/mentor")
MONGO_ID_REGEX = r"^[a-f\d]{24}$"


@router.get("/")
def get_all_mentors(credentials: HTTPAuthorizationCredentials = Depends(security)):
    mentors = users_collection.find({"role": "mentor"})
    return {"status": "success", "message": "Mentors Found Successfully", "mentors": list_serial(mentors)}


@router.get("/{id}")
def get_mentor(id: str = Path(description="Mentor id", pattern=MONGO_ID_REGEX), credentials: HTTPAuthorizationCredentials = Depends(security)):

    mentor = users_collection.find_one({"_id": ObjectId(id)})

    if mentor is None:
        raise HTTPException(status_code=404, detail="Mentee not found")

    return {"status": "success", "message": "Mentee found Successfully", "data": individual_serial(mentor)}


@router.put("update/{id}")
def update_mentor_profile(request: UpdateMentor, id: str = Path(description="Updates the Mentor info")):
    mentor = users_collection.find_one({"_id": ObjectId(id)})
    # if mentor is None:
    #   raise HTTPException(status_code=404, detail="Mentee not found")

    updated_mentor = users_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": request.dict()})

    return {"status": "success", "message": "Mentor Updated Successfully"}
