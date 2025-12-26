from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(255))
    email = Column(String(255), unique = True, index = True)
    phone_number = Column(String(20), nullable = True)
    password = Column(String(255))
    updated_at = Column(DateTime, default= datetime.now(timezone.utc), onupdate= datetime.now(timezone.utc), nullable= False)
    created_at = Column(DateTime, default= datetime.now(timezone.utc), nullable= False)
    
    sales = relationship('Sale', back_populates= 'user', cascade= 'all, delete')
    settings = relationship('Setting', back_populates= 'user', cascade= 'all, delete')