import math
from datetime import datetime

from dateutil.relativedelta import relativedelta
from sqlalchemy import func, text

from app.common.chart import get_pie_chart
from app.common.util import check_role_supervisor, is_invalid_order_by
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
    number_of_records = number_of_record
    page = page
    expire_period = expire_period
    periods = ["0-3 months", "3-6 months", "6-12 months", "over 12 months"]
    valid_fields = [
        "(0+contract_number)",
        "customer_name",
        "expire_date",
        "number_of_vehicles",
        "remaining_days",
    ]

    if expire_period not in periods:
        raise ValueError(f'Invalid expire_period "{expire_period}"')

    if is_invalid_order_by(order_by, valid_fields):
        raise ValueError("Invalid order_by")

    today = datetime.today()
    next_three_months = datetime.today() + relativedelta(months=3)
    next_six_months = datetime.today() + relativedelta(months=6)
    next_twelve_months = datetime.today() + relativedelta(months=12)

    data = (
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
    total = db.query(SaleInformation).join(Vehicle)

    if not check_role_supervisor(current_user):
        data = data.filter(
            Customer.company_id == Company.id,
            Customer.system_user == current_user.username,
        )
        total = total.filter(
            Customer.company_id == Company.id,
            Customer.system_user == current_user.username,
        )

    if expire_period == "0-3 months":
        data = data.filter(
            SaleInformation.end_date >= today,
            SaleInformation.end_date < next_three_months,
        )
        total = total.filter(
            Vehicle.sale_id == SaleInformation.id,
            SaleInformation.end_date >= today,
            SaleInformation.end_date < next_three_months,
        )

    if expire_period == "3-6 months":
        data = data.filter(
            SaleInformation.end_date >= next_three_months,
            SaleInformation.end_date < next_six_months,
        )
        total = total.filter(
            Vehicle.sale_id == SaleInformation.id,
            SaleInformation.end_date >= next_three_months,
            SaleInformation.end_date < next_six_months,
        )
    if expire_period == "6-12 months":
        data = data.filter(
            SaleInformation.end_date >= next_six_months,
            SaleInformation.end_date < next_twelve_months,
        )
        total = total.filter(
            Vehicle.sale_id == SaleInformation.id,
            SaleInformation.end_date >= next_six_months,
            SaleInformation.end_date < next_twelve_months,
        )
    if expire_period == "over 12 months":
        data = data.filter(SaleInformation.end_date >= next_twelve_months)

        total = total.filter(
            Vehicle.sale_id == SaleInformation.id,
            SaleInformation.end_date >= next_twelve_months,
        )

    data = (
        data.group_by(SaleInformation.sale_order_number)
        .order_by(text(order_by))
        .limit(number_of_records)
        .offset(int(number_of_records) * int(page))
        .all()
    )
    total = total.group_by(SaleInformation.sale_order_number).count()
    summary = {
        "value": math.ceil(total / int(number_of_records))
        if number_of_records != 0
        else 0,
        "label": "Page count",
        "datatype": "Int",
    }
    data = {"results": data, "summary": summary}
    return data
