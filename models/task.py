import datetime
from mongoengine import DateTimeField, Document
from .base import Base
from enum import Enum
from mongoengine import StringField, EnumField, IntField


class Status(Enum):
    In_progress = "in-progress"
    Completed = "completed"


class Task(Document, Base):
    employeeName = StringField()
    project = StringField()
    company_id = StringField()
    progress = IntField()
    status = EnumField(Status)
    created_at = DateTimeField()
    updated_at = DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        return super().save(*args, **kwargs)
