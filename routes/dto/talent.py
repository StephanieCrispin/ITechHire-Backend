from pydantic import BaseModel


class TalentRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class LoginTalentRequest(BaseModel):
    email: str
    password: str


class UpdateTalentEmail(BaseModel):
    new_email: str
    password: str


class UpdateTalentPassword(BaseModel):
    old_password: str
    new_password: str
