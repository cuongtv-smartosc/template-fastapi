from fastapi import APIRouter, Depends
from sqlalchemy import func, text
from sqlmodel import Session

from app.common.database import get_db
from app.common.util import get_chart
from app.models.sale_information import SaleInformation
from app.schemas.response import resp

sale_type_stats_router = APIRouter()

label_sale_type = ["Rent", "Sold", "Inventory (Used)", "Inventory (New)"]

SALE_TYPE_LABEL = {
    "rent": "Rent",
    "sold": "Sold",
    "inventory_used": "Inventory (Used)",
    "inventory_new": "Inventory (New)",
}


@sale_type_stats_router.get("/")
def sale_type_stats(db: Session = Depends(get_db)):
    data = (
        db.query(
            SaleInformation.sale_type,
            func.count(SaleInformation.id).label("count"),
        )
        .group_by(SaleInformation.sale_type)
        .order_by(text("count desc"))
        .all()
    )
    st = "sale_type"
    chart = get_chart(data, st, SALE_TYPE_LABEL, label_sale_type)
    return resp.success(data=chart)
