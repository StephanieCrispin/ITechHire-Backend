from pydantic import BaseModel
from models.task import Status


class TaskRequest(BaseModel):
    project: str
    progress: int
    status: Status


class UpdateTask(BaseModel):
    progress: int
