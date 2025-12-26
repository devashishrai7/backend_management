from sqlalchemy.orm import Session
from app.modules.dashboard.dashboard_model import Dashboard
from app.modules.dashboard.dashboard_schema import DashboardCreate

def createDashboard(data: DashboardCreate, db: Session):
    print(data)
    obj = Dashboard(field = data.field)
    db.add(obj)
    db.commit()
    return {
        'success' : True,
        'message' : 'Created successfully'
    }
    
def get(db: Session, user):
    data = db.query(Dashboard).all()
    return {
        'success' : True,
        'message' : 'Fetched successfully',
        'data' : data
    }