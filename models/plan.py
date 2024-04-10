from pydantic import BaseModel
from enum import Enum
from typing import Optional


class Duration(str, Enum):
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8


class Status(str, Enum):
    Pending = "pending"
    Accepted = "accepted"
    Rejected = "rejected"
    Complete = "complete"


class Plan(BaseModel):
    name: str
    duration: Duration
    status: Status = Status.Pending
    application: str
    mentee_id: Optional[str] = None
    mentor_email: str


class UpdatePlanModel(BaseModel):
    plan_id: Optional[str] = None
    status: Status
    mentee_id: Optional[str] = None
