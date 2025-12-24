from sqlalchemy.orm import Session
from app.modules.dashboard.dashboard_model import Dashboard
from app.modules.dashboard.dashboard_schema import DashboardCreate

def createDashboard(db: Session, data: DashboardCreate):
    obj = DashboardCreate(field = data.field)
    db.add(obj)
    db.commit()
    return {
        'success' : True,
        'message' : 'Created successfully'
    }
    
def get(db: Session):
    data = db.query(DashboardCreate).all()
    return {
        'success' : True,
        'message' : 'Fetched successfully',
        'data' : data
    }