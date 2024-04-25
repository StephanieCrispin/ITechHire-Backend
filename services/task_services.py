from models.task import Task
from bson import ObjectId
from fastapi import HTTPException, status


class TaskServices:
    """Utility class for handling common task logic"""

    @staticmethod
    def get_task_by_id(id: str):
        """Get task by id

        Args:
          id(ObjectId): task id
        """

        try:
            task = Task.objects.get(id=ObjectId(id))
            return task
        except Exception as e:
            raise e
            return None

    @staticmethod
    def get_tasks(id: str):
        """Get tasks belonging to company

        Args:
          id(ObjectId): company id
        """

        try:
            tasks = Task.objects.filter(company_id=id)
            return tasks
        except Exception as e:
            raise e
            return None

    @staticmethod
    def delete_task(id: str):
        """Deletes a task by a company

        Args:
        id (Objectid): task id
        """

        try:
            # Try to find the task by its ID
            task = Task.objects.get(id=ObjectId(id))
        except Task.DoesNotExist:
            # If the vacancy does not exist, raise a 404 error
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with id {id} not found"
            )

        # If the vacancy exists, delete it from the database
        task.delete()

    # @staticmethod
    # def get_completed_tasks(id: str):
    #     try:

    #         completed_tasks = Task.objects.filter(company_id=ObjectId(id))
    #         return completed_tasks
    #     except Exception as e:
    #         raise HTTPException(
    #             status_code=status.HTTP_400_BAD_REQUEST,
    #             detail=str(e))
