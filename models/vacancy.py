from mongoengine import DateTimeField, Document, StringField, EnumField
from mongoengine import ReferenceField, ListField
from .base import Base
import datetime
from enum import Enum
from .talent import Talent


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
    company_id = StringField()
    details = StringField()
    time = DateTimeField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

    def save(self, *args, **kwargs):
        if not self.time:
            self.time = datetime.datetime.now()
        return super().save(*args, **kwargs)


class SavedVacancy(Document, Base):
    talent = ReferenceField(Talent, required=True)
    vacancies = ListField(ReferenceField(Vacancy))
