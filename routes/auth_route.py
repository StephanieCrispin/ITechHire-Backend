from hashing import Hash
from fastapi import FastAPI, HTTPException, Depends, Request,status,APIRouter
from oauth import get_current_user
from jwttoken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from models.model import User,Login
from config.database import users_collection
from fastapi import APIRouter,status
from schemas.serializer import individual_serial
router = APIRouter()

@router.post("/sign-up",status_code=status.HTTP_201_CREATED)
def create_user(request:User):
  """
  Creates a new user object in the collection
  """
  # Reference this when doing any create function
  hashed_pass = Hash.bcrypt(request.password)

  user_object = dict(request)
  user_object["password"] = hashed_pass
  user_response = users_collection.insert_one(user_object)
  # response = individual_serial(user_response)

  # Ensure insertion was successful
  if user_response.acknowledged:
      # Retrieve the inserted document
      inserted_user = users_collection.find_one({"_id": user_response.inserted_id})
      return {"status":"success","data":individual_serial(inserted_user)}


@router.post("/login")
def login(request:Login):
  user = users_collection.find_one({"username":request.username})

  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  if not Hash.verify(user["password"], request.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  access_token = create_access_token(data={"sub":user["username"]})
  return {"data":individual_serial(user),"acccess_token":access_token,"token_type":"bearer" }