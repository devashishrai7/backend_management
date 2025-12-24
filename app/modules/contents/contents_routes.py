from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.modules.contents.contents_schema import Contents
from app.modules.contents.contents_controller import createContent, getContent

router = APIRouter(prefix= '/contents', tags= ['Contents'])

@router.post('/', summary= 'Create Contents')
def storeAnalytics(data: Contents, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return createContent(db, data)

@router.get('/', summary= 'Fetch Contents')
def fetchAnalytics(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return getContent(db)