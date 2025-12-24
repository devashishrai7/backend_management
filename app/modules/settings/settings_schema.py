from pydantic import BaseModel

class Settings(BaseModel):
    notification: bool
    offer_notification: bool