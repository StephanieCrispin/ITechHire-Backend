from models.company import Company
from bson import ObjectId

from models.employee import Employee
from models.vacancy import Vacancy
from models.task import Task, Status


class CompanyServices:
    """Utility class for handling common company logic"""

    @staticmethod
    def get_company_by_email(email: str):
        """Get company by email

        Args:
          email(str): user email
        """

        try:
            company = Company.objects(email=email).first()
            return company
        except Exception as e:
            raise e
            return None

    @staticmethod
    def get_company_by_id(id: str):
        """Get company by email

        Args:
          id(ObjectId): company id
        """

        try:
            company = Company.objects.get(id=ObjectId(id))
            return company
        except Exception as e:
            raise e
            return None

    @staticmethod
    def get_metrics(id: str):
        employees = Employee.objects.filter(
            company_id=id).count()
        vacancies = Vacancy.objects.filter(
            company_id=id).count()
        completed_tasks = completed_tasks = Task.objects.filter(
            company_id=id, status=Status.Completed).count()

        return {"total_employees": employees, "total_vacancies": vacancies,
                "completed_tasks": completed_tasks}
