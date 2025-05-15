from mongoengine import DateTimeField, Document, StringField, BooleanField
from .base import Base


class Company(Document, Base):

    """Request object"""

    name = StringField()
    email = StringField()
    logo = StringField()
    password = StringField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
    oauth_login = BooleanField(default=False)
