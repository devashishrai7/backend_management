from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.modules.leads.leads_schema import Leads
from app.modules.leads.leads_controller import createLead, getLead

router = APIRouter(prefix = '/leads', tags = ['Leads'])

@router.post('/create-lead', summary = 'Generate Leads')
def storeLead(data: Leads, db:Session = Depends(get_db)):
    return createLead(db, data)

@router.get('/', summary = 'Fetching Generated Leads')
def fetchLead(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return getLead(db)