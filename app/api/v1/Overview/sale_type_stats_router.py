from fastapi import APIRouter, Depends
from sqlalchemy import func, text
from sqlmodel import Session

from app.common.database import get_db
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

SALE_TYPE_COLOR = {
    "rent": "#0072DB",
    "sold": "#469BFF",
    "inventory_used": "#AAAFC7",
    "inventory_new": "#50CC65",
}


def get_chart(data):
    sale = "sale_type"
    labels = [SALE_TYPE_LABEL[i[sale]] if i[sale] else "" for i in data]
    values = [item["count"] for item in data]
    last_val = []
    for i in label_sale_type:
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
            "labels": label_sale_type,
            "datasets": [
                {
                    "name": "Number of Vehicles",
                    "values": last_val,
                }
            ],
            "colors": ["#0072DB", "#469BFF", "#AAAFC7", "#50CC65"],
        },
        "colors": ["#0072DB", "#469BFF", "#AAAFC7", "#50CC65"],
        "percent": percent,
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
    chart = get_chart(data)
    return resp.success(data=chart)
