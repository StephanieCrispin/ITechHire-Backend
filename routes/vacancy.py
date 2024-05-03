from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.vacancy import Vacancy, SavedVacancy
from routes.dto.vacancy import (VacancyRequest)
from services.company_services import CompanyServices
from services.vacancy_services import VacancyServices
from services.talent_services import TalentServices
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


@router.post("/save/${id}")
def update_saved(id: str, credentials:
                 HTTPAuthorizationCredentials = Depends(security)):
    """Saves a vacancy to a talent"""
    token = credentials.credentials
    payload = verify_token(token)

    talent = TalentServices.get_talent_by_id(payload["id"])
    vacancy = VacancyServices.get_vacancy(id)
    saved_vacancy = SavedVacancy.objects(talent=talent).first()

    if saved_vacancy:
        saved_vacancy.vacancies.append(vacancy)
    else:
        saved_vacancy = SavedVacancy(talent=talent, vacancies=[vacancy])

    saved_vacancy.save()

    return {"message": "Vacancy saved successfully"}


@router.get("")
def get_all_vacancies(credentials:
                      HTTPAuthorizationCredentials = Depends(security)):
    """Gets all vacancies belonging to a company"""

    token = credentials.credentials
    payload = verify_token(token)

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


@router.get("/talent/saved")
async def get_saved_vacancies(credentials: HTTPAuthorizationCredentials =
                              Depends(security)):
    """Gets all saved vacancies belonging to a talent"""

    token = credentials.credentials
    payload = verify_token(token)

    talent = TalentServices.get_talent_by_id(payload["id"])

    saved_vacancy = SavedVacancy.objects(talent=talent).first()

    if saved_vacancy:
        # return saved_vacancy.vacancies
        return [vacancy.to_dict() for vacancy in saved_vacancy.vacancies]
    else:
        return []


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


@router.delete("/saved/delete/{id}")
def delete_saved(id: str, credentials:
                 HTTPAuthorizationCredentials = Depends(security)):
    """Deletes a saved vacancy from a talent's list"""
    token = credentials.credentials
    payload = verify_token(token)

    talent = TalentServices.get_talent_by_id(payload["id"])
    vacancy = VacancyServices.get_vacancy(id)
    saved_vacancy = SavedVacancy.objects(talent=talent).first()

    if saved_vacancy:
        if vacancy in saved_vacancy.vacancies:
            saved_vacancy.vacancies.remove(vacancy)
            saved_vacancy.save()
            return [vacancy.to_dict() for vacancy in saved_vacancy.vacancies]

        else:
            raise HTTPException(
                status_code=404, detail="Vacancy not found in saved list")
    else:
        raise HTTPException(
            status_code=404, detail="No saved vacancies found for the talent")
