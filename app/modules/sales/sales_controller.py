from sqlalchemy.orm import Session
from app.modules.sales.sales_model import Sale
from app.modules.sales.sales_schema import Sales

def createSales(db: Session, data: Sales, user):
    obj = Sale(
        user_id = user.id,
        lead_id = data.lead_id,
        sale_status = data.sale_status
    )
    db.add(obj)
    db.commit()
    return {
        'success' : True,
        'message' : 'Sale done successfully!'
    }
    
def getSales(db: Session, user):
    data = db.query(Sale).filter(Sale.user_id == user.id).all()
    return {
        'success' : False,
        'message' : 'Fetched successfully!',
        'data' : data
    }