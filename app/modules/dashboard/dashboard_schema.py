from pydantic import BaseModel

class DashboardCreate(BaseModel):
    field: str