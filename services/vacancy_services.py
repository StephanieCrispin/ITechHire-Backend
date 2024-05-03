from models.vacancy import Vacancy
from fastapi import HTTPException, status
from bson import ObjectId
from .company_services import CompanyServices
# from bson.regex import Regex


class VacancyServices:

    """Utitlity class for Vacancy Services"""
    @staticmethod
    def get_all_vacancies(id: str):
        """Gets all current vacancies a company has posted

        Args:
        id (Objectid): company id
        """
        company = CompanyServices.get_company_by_id(ObjectId(id))
        if not company:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        try:
            vacancies = Vacancy.objects.filter(
                company_id=id).order_by('-created_at')

            return vacancies
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e))

    @staticmethod
    def get_total_vacancies():
        """Gets all  vacancies 

        Args:
        id (Objectid): company id
        """

        try:
            vacancies = Vacancy.objects().order_by('-time')

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

    @staticmethod
    def search_vacancies(search, skip=0):
        """Searches for vacancies by title using case-insensitive regex."""

        try:
            print(search)
            # Construct the regex pattern for case-insensitive search
            # Match any string containing the query, .* is for matching
            # Construct the regex pattern for case-insensitive search
            regex_pattern = f'.*{str(search)}.*'

            # Perform case-insensitive regex search on the title field
            vacancies = Vacancy.objects(title__iregex=regex_pattern).skip(
                skip).order_by('-time')
            return vacancies
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e))
