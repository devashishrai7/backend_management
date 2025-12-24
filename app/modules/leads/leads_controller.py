from sqlalchemy.orm import Session
from app.modules.leads.leads_model import Lead
from app.modules.leads.leads_schema import Leads

def createLead(db: Session, data: Leads):
    obj = Lead(
        name = data.name,
        email = data.email,
        phone_number = data.phone_number
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return {
        'success': True,
        'message': 'Thank you!'
    }

def getLead(db: Session):
    data = db.query(Lead).all()
    return {
        'success': True,
        'message': 'Fetched successfully',
        'data': data
    }