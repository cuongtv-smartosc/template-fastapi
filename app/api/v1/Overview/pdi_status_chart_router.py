from fastapi import APIRouter, Depends
from sqlalchemy import func, text
from sqlmodel import Session

from app.common.database import get_db
from app.common.util import get_chart
from app.models.electric_vehicle import Vehicle
from app.schemas.response import resp

pdi_status_chart_router = APIRouter()

labels_pdi_status = [
    "Shipping",
    "In Warehouse",
    "Assembled",
    "PDI completed",
    "Asset in inventory",
    "Delivered",
]
PDI_STATUS_LABEL = {
    "shipping": "Shipping",
    "in_warehouse": "In Warehouse",
    "assembled": "Assembled",
    "pdi_completed": "PDI completed",
    "asset_in_inventory": "Asset in inventory",
    "delivered": "Delivered",
}


@pdi_status_chart_router.get("/")
def pdi_status_chart(db: Session = Depends(get_db)):
    data = (
        db.query(
            Vehicle.forklift_pdi_status,
            func.count(Vehicle.id).label("count"),
        )
        .group_by(Vehicle.forklift_pdi_status)
        .order_by(text("count desc"))
        .all()
    )
    fps = "forklift_pdi_status"
    chart = get_chart(data, fps, PDI_STATUS_LABEL, labels_pdi_status)
    return resp.success(data=chart)
