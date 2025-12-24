from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from enum import Enum as pyEnum
from app.database import Base

class SaleStatus(str, pyEnum):
    sale = 'sale'
    reject = 'reject'


class Sale(Base):
    __tablename__ = 'sales'
    
    id = Column(Integer, primary_key= True, index= True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete= 'CASCADE'), nullable= False)
    lead_id = Column(Integer, ForeignKey('leads.id', ondelete= 'CASCADE'), nullable= False)
    sale_status = Column(Enum(SaleStatus, name = 'sale_status_enum'), nullable= False)
    updated_at = Column(DateTime, default= datetime.now(timezone.utc), onupdate= datetime.now(timezone.utc), nullable= False)
    created_at = Column(DateTime, default= datetime.now(timezone.utc), nullable= False)
    
    
    user = relationship('User', back_populates= 'sales')
    lead = relationship('Lead', back_populates= 'sales')