from fastapi import APIRouter, Depends
from sqlalchemy import func, text
from sqlmodel import Session

from app.common.database import get_db
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

PDI_STATUS_COLOR = {
    "shipping": "#469BFF",
    "in_warehouse": "rgba(70, 155, 255, 0.7)",
    "assembled": "#AAAFC7",
    "pdi_completed": "#FFC459",
    "asset_in_inventory": "#FC6563",
    "delivered": "rgba(80, 204, 101, 0.7)",
}


def get_chart(data):
    fps = "forklift_pdi_status"
    labels = [PDI_STATUS_LABEL[i[fps]] if i[fps] else "" for i in data]
    values = [item["count"] for item in data]
    last_val = []
    for i in labels_pdi_status:
        if i in labels:
            index_label = labels.index(i)
            last_val.append(values[index_label])
        else:
            last_val.append(0)
    percent = []
    for i in last_val:
        if sum(last_val) != 0:
            percent.append((i / sum(last_val)) * 100)
        else:
            percent.append(0)

    return {
        "type": "pie",
        "data": {
            "labels": labels_pdi_status,
            "datasets": [
                {
                    "name": "Number of Vehicles",
                    "values": last_val,
                }
            ],
            "colors": [
                "#469BFF",
                "rgba(70, 155, 255, 0.7)",
                "#AAAFC7",
                "#FFC459",
                "#FC6563",
                "rgba(80, 204, 101, 0.7)",
            ],
        },
        "colors": [
            "#469BFF",
            "rgba(70, 155, 255, 0.7)",
            "#AAAFC7",
            "#FFC459",
            "#FC6563",
            "rgba(80, 204, 101, 0.7)",
        ],
        "percent": percent,
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

    chart = get_chart(data)
    return resp.success(data=chart)
