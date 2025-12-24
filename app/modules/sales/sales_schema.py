from pydantic import BaseModel
from app.modules.sales.sales_model import SaleStatus

class Sales(BaseModel):
    lead_id : int
    sale_status : SaleStatus