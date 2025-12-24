from pydantic import BaseModel

class Contents(BaseModel):
    subject: str
    description: str