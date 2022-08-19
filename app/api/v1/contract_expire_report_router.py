import json
import math
from datetime import datetime

from dateutil.relativedelta import relativedelta
from fastapi import APIRouter, Depends
from sqlalchemy import func, text
from sqlmodel import Session

from app.common.database import get_db
from app.common.util import is_invalid_order_by
from app.models.customer import Customer
from app.models.electric_vehicle import Vehicle
from app.models.sale_information import SaleInformation
from app.schemas.response import resp

contract_expire_router = APIRouter()


@contract_expire_router.get("/")
def contract_expire_report(filters=None, db: Session = Depends(get_db)):
    if not isinstance(filters, dict):
        filters = json.loads(filters)
    order_by = (
        f'{filters.get("sort_by", "remaining_days")} '
        f'{filters.get("sort_order", "asc")}'
    )
    if filters.get("sort_by") == "contract_number":
        order_by = f'(0+contract_number) {filters.get("sort_order", "asc")}'
    number_of_records = filters.get("number_of_record", "5")
    print(number_of_records)
    page = filters.get("page", "0")
    expire_period = filters.get("expire_period", "0-3 months")
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
            SaleInformation.sale_order_number,
            Customer.customer_name,
            func.count(Vehicle.id),
            SaleInformation.end_date,
            func.datediff(SaleInformation.end_date, func.current_date()).label(
                "remaining_days"
            ),
        )
        .join(Customer, SaleInformation.customer_id == Customer.id)
        .join(Vehicle, SaleInformation.id == Vehicle.sale_id)
    )
    total = db.query(SaleInformation).join(Vehicle)
    if expire_period == "0-3 months":
        data.filter(
            SaleInformation.end_date >= today,
            SaleInformation.end_date < next_three_months,
        )
        total.filter(
            Vehicle.sale_id == SaleInformation.id,
            SaleInformation.end_date >= today,
            SaleInformation.end_date < next_three_months,
        )
    if expire_period == "3-6 months":
        data.filter(
            SaleInformation.end_date >= next_three_months,
            SaleInformation.end_date < next_six_months,
        )
        total.filter(
            Vehicle.sale_id == SaleInformation.id,
            SaleInformation.end_date >= next_three_months,
            SaleInformation.end_date < next_six_months,
        )
    if expire_period == "6-12 months":
        data.filter(
            SaleInformation.end_date >= next_six_months,
            SaleInformation.end_date < next_twelve_months,
        )
        total.filter(
            Vehicle.sale_id == SaleInformation.id,
            SaleInformation.end_date >= next_six_months,
            SaleInformation.end_date < next_twelve_months,
        )
    if expire_period == "over 12 months":
        data.filter(SaleInformation.end_date >= next_twelve_months)
        total.filter(
            Vehicle.sale_id == SaleInformation.id,
            SaleInformation.end_date >= next_twelve_months,
        )
    data = (
        data.group_by(SaleInformation.sale_order_number)
        .order_by(text(order_by))
        .limit(number_of_records)
        .offset(number_of_records * int(page))
        .all()
    )
    total = total.distinct(SaleInformation.sale_order_number).count()

    summary = {
        "value": math.ceil(total / int(number_of_records))
        if number_of_records != 0
        else 0,
        "label": "Page count",
        "datatype": "Int",
    }
    data = {"data": data, "summary": summary}
    return resp.success(data=data)
