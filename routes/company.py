from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.hashing import Hash
from models.company import Company
from services.company_services import CompanyServices
from routes.dto.company import (CompanyRequest, LoginCompany)
from utils.jwt_service import create_access_token, verify_token

router = APIRouter()
security = HTTPBearer()


@router.post("/create", status_code=201)
async def create_company(body: CompanyRequest):
    """Create a new company document in the database"""

    body.password = Hash.hash_password(body.password)

    company = Company(
        name=body.name,
        email=body.email,
        logo=body.logo,
        password=body.password
    )
    try:
        company.save()
    except Exception as e:
        print(e)
        company.delete()
        raise HTTPException(
            status_code=500, detail="Email already exists"
        ) from e

    return company.to_dict()


@router.post("/login")
async def login_company(body: LoginCompany):

    company = CompanyServices.get_company_by_email(body.email)

    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not Hash.verify_password(body.password, company.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    access_token = create_access_token(
        data={"id": company.to_dict()["_id"],
              "email": company.to_dict()["email"]})
    return {
        "company": company.to_dict(),
        "access_token": access_token
    }


@router.get("/metrics")
async def get_metrics(credentials:
                      HTTPAuthorizationCredentials = Depends(security)):
    """Gets the metrics for a company"""
    token = credentials.credentials
    payload = verify_token(token)
    print(payload["id"])

    try:
        metrics = CompanyServices.get_metrics(payload['id'])
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, detail="Problem with getting metric"
        ) from e
    return metrics
