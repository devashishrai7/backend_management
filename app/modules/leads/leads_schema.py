from pydantic import BaseModel, EmailStr

class Leads(BaseModel):
    name: str
    email: EmailStr
    phone_number: int