from pydantic import BaseModel


class CompanyRequest(BaseModel):
    name: str
    email: str
    logo: str
    password: str


class LoginCompany(BaseModel):
    email: str
    password: str
