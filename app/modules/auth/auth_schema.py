from pydantic import BaseModel, EmailStr, field_validator
import re

class Register(BaseModel):
    name: str
    email: EmailStr
    phone_number: int | None = None
    password: str
    
    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*(),.?\":{}|<>]).{8,}$"
        if not re.match(pattern, password):
            raise ValueError(
                "Password must be at least 8 characters long and include "
                "one uppercase, one lowercase, and one special character"
            )
        return password

class Login(BaseModel):
    email: EmailStr
    password: str