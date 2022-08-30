from sqlalchemy import func, text

from app.common.chart import get_pie_chart
from app.models.electric_vehicle import Vehicle
from app.models.sale_information import SaleInformation

SALE_TYPE_LABEL = {
    "rent": "Rent",
    "sold": "Sold",
    "inventory_used": "Inventory (Used)",
    "inventory_new": "Inventory (New)",
}
SALE_TYPE_COLOR = [
    "#0072DB",
    "#469BFF",
    "#AAAFC7",
    "#50CC65",
]

PDI_STATUS_LABEL = {
    "shipping": "Shipping",
    "in_warehouse": "In Warehouse",
    "assembled": "Assembled",
    "pdi_completed": "PDI completed",
    "asset_in_inventory": "Asset in inventory",
    "delivered": "Delivered",
}
PDI_STATUS_COLOR = [
    "#469BFF",
    "rgba(70, 155, 255, 0.7)",
    "#AAAFC7",
    "#FFC459",
    "#FC6563",
    "rgba(80, 204, 101, 0.7)",
]


def sale_type_stat(db):
    label_sale_type = list(SALE_TYPE_LABEL.values())
    data = (
        db.query(
            SaleInformation.sale_type,
            func.count(SaleInformation.id).label("count"),
        )
        .group_by(SaleInformation.sale_type)
        .order_by(text("count desc"))
        .all()
    )
    chart = get_pie_chart(
        data,
        SALE_TYPE_COLOR,
        "sale_type",
        SALE_TYPE_LABEL,
        label_sale_type,
    )
    return chart


def pdi_status_chart(db):
    labels_pdi_status = list(PDI_STATUS_LABEL.values())
    data = (
        db.query(
            Vehicle.forklift_pdi_status,
            func.count(Vehicle.id).label("count"),
        )
        .group_by(Vehicle.forklift_pdi_status)
        .order_by(text("count desc"))
        .all()
    )
    chart = get_pie_chart(
        data,
        PDI_STATUS_COLOR,
        "forklift_pdi_status",
        PDI_STATUS_LABEL,
        labels_pdi_status,
    )
    return chart
