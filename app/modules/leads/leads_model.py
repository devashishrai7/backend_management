from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.database import Base

class Lead(Base):
    __tablename__ = 'leads'
    
    id = Column(Integer, primary_key= True, index= True)
    name = Column(String(50))
    email = Column(String(150), nullable= True)
    phone_number = Column(Integer, nullable= True)
    updated_at = Column(DateTime, default= datetime.now(timezone.utc), onupdate= datetime.now(timezone.utc), nullable= False)
    created_at = Column(DateTime, default= datetime.now(timezone.utc), nullable= False)