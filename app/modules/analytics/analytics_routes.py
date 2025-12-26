from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.modules.analytics.analytics_schema import Create
from app.modules.analytics.analytics_controller import createAnalytics, getAnalytics

router = APIRouter(prefix= '/analytics', tags= ['Analytics'])

@router.post('/', summary= 'Create Authenticated User\'s Analytics', status_code= status.HTTP_201_CREATED)
def storeAnalytics(data: Create, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return createAnalytics(db, data)

@router.get('/', summary= 'Fetch Authenticated User\'s Analytics')
def fetchAnalytics(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return getAnalytics(db)