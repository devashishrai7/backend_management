from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.modules.sales.sales_controller import createSales, getSales
from app.modules.sales.sales_schema import Sales

router = APIRouter(prefix= '/sales', tags= ['Sales'])

@router.post('/', summary= 'Generate Sales', status_code= status.HTTP_201_CREATED)
def storeSales(data: Sales, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return createSales(db, data, user)

@router.get('/', summary= 'Fetch Authenticated User\'s Sales')
def fetchSales(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return getSales(db, user)