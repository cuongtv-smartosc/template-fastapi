from sqlalchemy import func, text

from app.common.chart import get_pie_chart
from app.models.electric_vehicle import Vehicle
from app.models.sale_information import SaleInformation

label_sale_type = ["Rent", "Sold", "Inventory (Used)", "Inventory (New)"]

SALE_TYPE_LABEL = {
    "rent": "Rent",
    "sold": "Sold",
    "inventory_used": "Inventory (Used)",
    "inventory_new": "Inventory (New)",
}

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


def sale_type_stat(db):
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
    chart = get_pie_chart(data, st, SALE_TYPE_LABEL, label_sale_type)
    return chart


def pdi_status_chart(db):
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
    chart = get_pie_chart(data, fps, PDI_STATUS_LABEL, labels_pdi_status)
    return chart
