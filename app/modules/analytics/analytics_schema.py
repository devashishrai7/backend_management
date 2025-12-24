from pydantic import BaseModel

class Create(BaseModel):
    subject: str
    description: str