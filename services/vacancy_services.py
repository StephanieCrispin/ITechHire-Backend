from models.vacancy import Vacancy
from fastapi import HTTPException, status
from bson import ObjectId
from .company_services import CompanyServices


class VacancyServices:

    """Utitlity class for Vacancy Services"""
    @staticmethod
    def get_al_vacancies(id: str):
        """Gets all current vacancies a company has posted

        Args:
        id (Objectid): company id
        """
        company = CompanyServices.get_company_by_id(ObjectId(id))
        if not company:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        try:
            vacancies = Vacancy.objects.filter(
                company_id=company.to_dict()["_id"])

            return vacancies
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e))

    @staticmethod
    def delete_a_vacancy(id: str):
        """Deletes a vacancy by a company

        Args:
        id (Objectid): vacancy id
        """

        try:
            # Try to find the vacancy by its ID
            vacancy = Vacancy.objects.get(id=ObjectId(id))
        except Vacancy.DoesNotExist:
            # If the vacancy does not exist, raise a 404 error
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Vacancy with id {id} not found"
            )

        # If the vacancy exists, delete it from the database
        vacancy.delete()

    @staticmethod
    def get_vacancy(id: str):
        """Gets a vacancy by a company

        Args:
        id (Objectid): vacancy id
        """

        try:
            # Try to find the vacancy by its ID
            vacancy = Vacancy.objects.get(id=ObjectId(id))
            return vacancy
        except Vacancy.DoesNotExist:
            # If the vacancy does not exist, raise a 404 error
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Vacancy with id {id} not found"
            )
