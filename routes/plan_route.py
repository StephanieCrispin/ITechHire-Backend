from fastapi import HTTPException, Request, status, APIRouter, Path, Depends
from models.plan import Plan as PlanModel, UpdatePlanModel
from config.database import plan_collection, users_collection
from schemas.plan_serializer import individual_serial, list_serial
from jwttoken import verify_token
from bson.objectid import ObjectId
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.user import Role
router = APIRouter(prefix="/plan")
security = HTTPBearer()


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_plan(request: PlanModel, credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """
    Creates a new plan object in the collection
    """
    token = credentials.credentials
    payload = verify_token(token)

    # Check if useremail already exists
    user = users_collection.find_one(
        {"_id": ObjectId(payload["id"])})

    mentor = users_collection.find_one(
        {"email": request.mentor_email, "role": Role.Mentor})

    if user is None or mentor is None:
        raise HTTPException(status_code=404, detail="User or Mentor not found")

    request.mentee_id = payload["id"]
    plan_object = dict(request)

    plan_response = plan_collection.insert_one(plan_object)

    # Ensure insertion was successful
    if plan_response.acknowledged:
        print(plan_response)

        # Retrieve the inserted document
        inserted_plan = plan_collection.find_one(
            {"_id": plan_response.inserted_id})
        return {"status": "success", "messag": "Plan created successfully",
                "data": individual_serial(inserted_plan)}


@router.put("/update-status")
def update_status(request: UpdatePlanModel, credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """
    Updates the status of a plan
    """
    # Check if useremail already exists
    user = users_collection.find_one(
        {"_id": ObjectId(request.mentee_id)})

    print(user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    plan_collection.update_one(
        {"_id": request.plan_id, "mentee_id": ObjectId(user["_id"])},
        {"$set": request.dict()})

    return {"status": "success", "message": "Plan Updated Successfully"}


@router.get("/all")
def get_all_plans(credentials: HTTPAuthorizationCredentials = Depends(security)):
    plans = plan_collection.find()
    return {"status": "success", "message": "Plans Found Successfully", "plans": list_serial(plans)}
