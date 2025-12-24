from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.modules.settings.settings_controller import updateSetting, getSettings
from app.modules.settings.settings_schema import Settings

router = APIRouter(prefix= '/settings', tags= ['Setting'])

@router.put('/', summary= "To Update Authenticated User's Settings")
def storeSetting(data: Settings, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return updateSetting(db, data, user)

@router.get('/', summary= "To Fetch Authenticated User's Settings")
def fetchSettings(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return getSettings(db, user)