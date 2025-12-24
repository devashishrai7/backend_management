from sqlalchemy.orm import Session
from app.modules.analytics.analytics_model import Analytic
from app.modules.analytics.analytics_schema import Create

def createAnalytics(db: Session, data:Create):
    obj = Analytic(
        subject = data.subject,
        description = data.description
    )
    db.add(obj)
    db.commit()
    return {
        'success' : True,
        'message' : 'Analytics created!'
    }

def getAnalytics(db: Session):
    data = db.query(Analytic).all()
    return {
        'success' : True,
        'message' : 'Data fetched successfully',
        'data' : data
    }
    
