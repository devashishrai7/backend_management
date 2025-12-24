from sqlalchemy.orm import Session
from app.modules.settings.settings_model import Setting
from app.modules.settings.settings_schema import Settings

def updateSetting(db: Session, data: Settings, user):
    obj = Setting(
        user_id = user.id,
        notification = data.notification,
        offer_notification = data.offer_notification
    )
    db.add(obj)
    db.commit()
    return {
        'success': True,
        'message' : 'Settings updated successfully'
    }
    
def getSettings(db:Session, user):
    data = db.query(Setting).filter(Setting.user_id == user.id).first()
    return {
        'success' : True,
        'message' : 'Settings fetched successfully',
        'data' : data
    }