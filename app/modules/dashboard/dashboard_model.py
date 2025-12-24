from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.database import Base

class Dashboard(Base):
    __tablename__ = 'dashboard'
    
    id = Column(Integer, primary_key= True, index= True)
    field = Column(String(200))
    updated_at = Column(DateTime, default= datetime.now(timezone.utc), onupdate= datetime.now(timezone.utc), nullable= False)
    created_at = Column(DateTime, default= datetime.now(timezone.utc), nullable= False)