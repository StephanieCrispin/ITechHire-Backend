from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.employee import Employee
from routes.dto.employee import (EmployeeRequest)
from services.company_services import CompanyServices
from services.employee_services import EmployeeServices
from utils.jwt_service import verify_token

router = APIRouter()
security = HTTPBearer()


@router.post("/create", status_code=200)
async def create_employee(body: EmployeeRequest, credentials:
                          HTTPAuthorizationCredentials = Depends(security)):
    """Creates a new employee docuement in database"""
    token = credentials.credentials
    payload = verify_token(token)

    company = CompanyServices.get_company_by_id(payload["id"])

    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    employee = Employee(
        name=body.name,
        email=body.email,
        company_id=company.to_dict()["_id"]
    )
    try:
        employee.save()
    except Exception as e:
        print(e)
        employee.delete()
        raise HTTPException(
            status_code=500, detail="Company doesn't exist"
        ) from e

    return employee.to_dict()


@router.get("")
async def get_employees(credentials:
                        HTTPAuthorizationCredentials = Depends(security)):
    """Gets all employees belonging to a company"""
    token = credentials.credentials
    payload = verify_token(token)
    print(payload["id"])

    try:
        employees = EmployeeServices.get_all_employees(payload["id"])
    except Exception as e:
        print(e)

        raise HTTPException(
            status_code=500, detail="Problem with getting eployees"
        ) from e

    return [employee.to_dict() for employee in employees]
