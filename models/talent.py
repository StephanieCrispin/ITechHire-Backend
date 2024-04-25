from mongoengine import DateTimeField, Document, StringField
from .base import Base


class Talent(Document, Base):

    """Request object"""
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    password = StringField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
