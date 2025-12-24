from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.modules.dashboard.dashboard_controller import createDashboard, get
from app.modules.dashboard.dashboard_schema import DashboardCreate

router = APIRouter(prefix= '/dashboard', tags= ['Dashboard'])

@router.post('/', summary= 'Create Dashboard')
def store(data: DashboardCreate, db: Session = Depends(get_db)):
    return createDashboard(data, db)

@router.get('/', summary= 'Fetch Dashboard')
def fetch(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return get(db, user)