from sqlalchemy import Column, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class Setting(Base):
    __tablename__ = 'settings'    
    
    id = Column(Integer, primary_key= True, index= True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete= 'CASCADE'), nullable= False, unique= True)
    notification = Column(Boolean, nullable= False, default= True)
    offer_notification = Column(Boolean, nullable= False, default= True)
    updated_at = Column(DateTime, default= datetime.now(timezone.utc), onupdate= datetime.now(timezone.utc), nullable= False)
    created_at = Column(DateTime, default= datetime.now(timezone.utc), nullable= False)
    
    user = relationship('User', back_populates= 'settings')