from mongoengine import DateTimeField, Document, StringField
from .base import Base
import datetime


class Employee(Document, Base):

    """Request object"""

    name = StringField()
    email = StringField()
    company_id = StringField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        return super().save(*args, **kwargs)
