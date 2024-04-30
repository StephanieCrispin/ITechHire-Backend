from models.employee import Employee
from fastapi import HTTPException, status
from bson import ObjectId
from .company_services import CompanyServices


class EmployeeServices:
    """Utility class for handling common employee logic"""

    @staticmethod
    def get_all_employees(id: str):
        """Get all employees in a company

            Args:
          id(ObjectId): company id
        """

        # try:
        company = CompanyServices.get_company_by_id(ObjectId(id))
        if not company:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        try:
            employees = Employee.objects.filter(
                company_id=company.to_dict()["_id"]).order_by('-created_at')

            return employees
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e))

    @staticmethod
    def get_employee_by_id(id: str):
        """Get employee by id

        Args:
          id(ObjectId): employee id
        """

        try:
            company = Employee.objects.get(id=ObjectId(id))
            return company
        except Exception as e:
            raise e
            return None
