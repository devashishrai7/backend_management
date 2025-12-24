from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.database import Base

class Analytic(Base):
    __tablename__ = "analytics"
    
    id = Column(Integer, primary_key= True, index= True)
    subject = Column(String(150))
    description = Column(String(255))
    updated_at = Column(DateTime, default= datetime.now(timezone.utc), onupdate= datetime.now(timezone.utc), nullable= False)
    created_at = Column(DateTime, default= datetime.now(timezone.utc), nullable= False)