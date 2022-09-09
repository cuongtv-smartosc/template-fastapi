import math

from sqlalchemy import func, text

from app.common.chart import get_pie_chart
from app.common.util import check_role_supervisor, get_date_from_period
from app.models.company import Company
from app.models.customer import Customer
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


def vehicle_by_location(
    page,
    number_of_record,
    sort_by,
    sort_order,
    db,
    current_user,
):
    order_by = f"{sort_by} {sort_order}"
    order_by_more = "location asc"

    query = db.query(
        SaleInformation.location.label("location"),
        func.count(Vehicle.id).label("number_of_vehicles"),
    ).join(SaleInformation, Vehicle.sale_id == SaleInformation.id)

    if not check_role_supervisor(current_user):
        query = query.join(
            Customer,
            SaleInformation.customer_id == Customer.id,
        ).filter(
            Customer.system_user == current_user.username,
        )
    offset = int(number_of_record) * int(page)

    query = (
        query.filter(SaleInformation.location != "")
        .group_by(SaleInformation.location)
        .order_by(text(order_by), text(order_by_more))
    )

    data = query.offset(offset).limit(int(number_of_record) + offset).all()
    total_page = math.ceil(len(query.all()) / int(number_of_record))

    summary = {
        "current_page": page + 1 if total_page != 0 else 0,
        "total_page": total_page,
    }
    return {"results": data, "summary": summary}


def contract_expire_report(
    page,
    number_of_record,
    expire_period,
    sort_by,
    sort_order,
    db,
    current_user,
):
    order_by = f"{sort_by} " f"{sort_order}"
    if sort_by == "contract_number":
        order_by = f"(0+contract_number) {sort_order}"

    query = (
        db.query(
            SaleInformation.sale_order_number.label("contract_number"),
            Customer.customer_name.label("customer_name"),
            func.count(Vehicle.id).label("number_of_vehicles"),
            SaleInformation.end_date.label("expire_date"),
            func.datediff(SaleInformation.end_date, func.current_date()).label(
                "remaining_days"
            ),
        )
        .join(Customer, SaleInformation.customer_id == Customer.id)
        .join(Vehicle, SaleInformation.id == Vehicle.sale_id)
    )

    if not check_role_supervisor(current_user):
        query = query.filter(
            Customer.company_id == Company.id,
            Customer.system_user == current_user.username,
        )

    from_date, to_date = get_date_from_period(expire_period)
    query = query.filter(SaleInformation.end_date >= from_date)
    if to_date is not None:
        query = query.filter(SaleInformation.end_date <= to_date)

    total = query.group_by(SaleInformation.sale_order_number).count()
    query = (
        query.group_by(SaleInformation.sale_order_number)
        .order_by(text(order_by))
        .limit(number_of_record)
        .offset(int(number_of_record) * int(page))
        .all()
    )
    total_page = math.ceil(total / int(number_of_record))

    summary = {
        "current_page": page + 1 if number_of_record != 0 else 0,
        "total_page": total_page,
    }
    return {"results": query, "summary": summary}
