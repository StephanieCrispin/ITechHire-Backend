from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.task import Task, Status
from routes.dto.task import (UpdateTask, TaskRequest)
from services.company_services import CompanyServices
from services.employee_services import EmployeeServices
from utils.jwt_service import verify_token
from services.task_services import TaskServices

router = APIRouter()
security = HTTPBearer()


@router.post("/create/{employee_id}", status_code=200)
async def create_task(employee_id: str, body: TaskRequest, credentials:
                      HTTPAuthorizationCredentials = Depends(security)):
    """Creates a new task docuement in database"""
    token = credentials.credentials
    payload = verify_token(token)
    print(payload["id"])

    company = CompanyServices.get_company_by_id(payload["id"])
    employee = EmployeeServices.get_employee_by_id(employee_id)
    if not company or not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    task = Task(
        employeeName=employee.to_dict()['name'],
        project=body.project,
        progress=body.progress,
        company_id=company.to_dict()["_id"],
    )
    if int(body.progress) == 100:
        task.status = Status.Completed
    else:
        task.status = Status.In_progress
    try:
        task.save()
    except Exception as e:
        print(e)
        task.delete()
        raise HTTPException(
            status_code=500, detail="Task doesn't exist"
        ) from e

    return task.to_dict()


@router.get("")
async def get_tasks(credentials:
                    HTTPAuthorizationCredentials = Depends(security)):
    """Gets all tasks belonging to a company"""
    token = credentials.credentials
    payload = verify_token(token)
    print(payload["id"])

    try:
        tasks = TaskServices.get_tasks(payload["id"])
    except Exception as e:
        print(e)

        raise HTTPException(
            status_code=500, detail="Problem with getting tasks"
        ) from e

    return [task.to_dict() for task in tasks]


@router.put('/update/{task_id}')
async def update_task(task_id: str, body: UpdateTask, credentials:
                      HTTPAuthorizationCredentials = Depends(security)):
    """Updates a task document in the database"""
    task = TaskServices.get_task_by_id(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    task.progress = body.progress

    if int(body.progress) == 100:
        task.status = Status.Completed
    else:
        task.status = Status.In_progress

    task.save()

    return task.to_dict()


@router.delete("/delete/{id}")
def deletes_a_task(id: str, credentials:
                   HTTPAuthorizationCredentials = Depends(security)):
    """Deletes a specific task belonging to a company)"""

    try:
        TaskServices.delete_task(id)
    except Exception as e:
        print(e)

        raise HTTPException(
            status_code=500, detail="Problem with deleting task"
        ) from e

    return {"status": "true", "message": "Task deleted"}
