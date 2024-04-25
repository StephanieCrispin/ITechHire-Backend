from pydantic import BaseModel
from models.vacancy import WorkMode, JobType


class VacancyRequest(BaseModel):
    location: str
    amount: str
    link: str
    title: str
    jobType: JobType
    commitment: str
    details: str
    mode: WorkMode
