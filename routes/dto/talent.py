from pydantic import BaseModel


class TalentRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class LoginTalentRequest(BaseModel):
    email: str
    password: str
