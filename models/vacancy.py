from mongoengine import DateTimeField, Document, StringField, EnumField
from .base import Base
import datetime
from enum import Enum


class JobType(Enum):
    Full_time = "full-time"
    Part_time = "part-time"
    Contract = "contract"
    Freelance = "freelance"
    Internship = "internship"


class WorkMode(Enum):
    Remote = "remote"
    Hybrid = "hybrid"
    Onsite = "onsite"


class Vacancy(Document, Base):

    """vacancy object"""

    location = StringField()
    companyPicture = StringField()
    companyName = StringField()
    amount = StringField()
    link = StringField()
    title = StringField()
    mode = EnumField(WorkMode)
    jobType = EnumField(JobType)
    commitment = StringField()
    company_id = StringField()
    details = StringField()
    time = DateTimeField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

    def save(self, *args, **kwargs):
        if not self.time:
            self.time = datetime.datetime.now()
        return super().save(*args, **kwargs)
