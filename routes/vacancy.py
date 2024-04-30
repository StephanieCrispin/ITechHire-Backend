from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.vacancy import Vacancy
from routes.dto.vacancy import (VacancyRequest)
from services.company_services import CompanyServices
from services.vacancy_services import VacancyServices
from utils.jwt_service import verify_token

router = APIRouter()
security = HTTPBearer()


@router.post("/create", status_code=201)
async def create_vacancy(body: VacancyRequest, credentials:
                         HTTPAuthorizationCredentials = Depends(security)):
    """Creates a new vacancy docuement in database"""
    token = credentials.credentials
    payload = verify_token(token)
    print(payload["id"])

    company = CompanyServices.get_company_by_id(payload["id"])

    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    vacancy = Vacancy(
        location=body.location,
        companyPicture=company.logo,
        companyName=company.name,
        amount=body.amount,
        link=body.link,
        title=body.title,
        jobType=body.jobType,
        company_id=company.to_dict()["_id"],
        details=body.details,
        mode=body.mode
    )

    try:
        vacancy.save()
    except Exception as e:
        print(e)
        vacancy.delete()
        raise HTTPException(
            status_code=500, detail="Company doesn't exist"
        ) from e
    return vacancy.to_dict()


@router.get("")
def get_all_vacancies(credentials:
                      HTTPAuthorizationCredentials = Depends(security)):
    """Gets all vacancies belonging to a company"""

    token = credentials.credentials
    payload = verify_token(token)
    print(payload["id"])

    try:
        vacancies = VacancyServices.get_all_vacancies(payload["id"])
    except Exception as e:
        print(e)

        raise HTTPException(
            status_code=500, detail="Problem with getting all vacancies"
        ) from e
    return [vacancy.to_dict() for vacancy in vacancies]


@router.get("/custom")
def custom_vacancies(search: str | None = None, limit: int = 0, credentials:
                     HTTPAuthorizationCredentials = Depends(security)):
    """Searches for vacancy with title"""
    print(f"from routes {search}")
    try:
        vacancies = VacancyServices.search_vacancies(search, limit)
    except Exception as e:
        print(e)

        raise HTTPException(
            status_code=500, detail="Problem with getting all vacancies"
        ) from e
    return [vacancy.to_dict() for vacancy in vacancies]


@router.get("/total")
def get_total_vacancies(credentials:
                        HTTPAuthorizationCredentials = Depends(security)):
    """Gets total vacancies"""

    try:
        vacancies = VacancyServices.get_total_vacancies()
    except Exception as e:
        print(e)

        raise HTTPException(
            status_code=500, detail="Problem with getting all vacancies"
        ) from e
    return [vacancy.to_dict() for vacancy in vacancies]


@router.get("/{id}")
def get_vacancy(id: str, credentials:
                HTTPAuthorizationCredentials = Depends(security)):
    """Gets vacancy belonging to a company"""

    try:
        vacancy = VacancyServices.get_vacancy(id)
    except Exception as e:
        print(e)

        raise HTTPException(
            status_code=500, detail="Problem with getting all vacancies"
        ) from e
    return vacancy.to_dict()


@router.delete("/delete/{id}")
def delete_all_vacancies(id: str, credentials:
                         HTTPAuthorizationCredentials = Depends(security)):
    """Deletes a specific vacancy belonging to a company)"""

    try:
        VacancyServices.delete_a_vacancy(id)
    except Exception as e:
        print(e)

        raise HTTPException(
            status_code=500, detail="Problem with deleting vacancy"
        ) from e

    return {"status": "true", "message": "Vacancy deleted"}
