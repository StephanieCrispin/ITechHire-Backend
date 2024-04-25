from mongoengine import DateTimeField, Document, StringField
from .base import Base


class Employee(Document, Base):

    """Request object"""

    name = StringField()
    email = StringField()
    company_id = StringField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
