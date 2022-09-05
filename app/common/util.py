from datetime import datetime

from dateutil.relativedelta import relativedelta

from app.common.database import SessionLocal
from app.models.company import Company
from app.models.customer import Customer
from app.models.user import User


def validate_unique(table, field, **kwargs):
    session = SessionLocal()
    q = session.query(getattr(table, field)).filter_by(**kwargs).scalar()
    session.close()
    if q:
        raise ValueError(f"""Table {table.__name__} {field} already exist""")
    return kwargs[field]


array_data = [
    "0-3 months",
    "3-6 months",
    "6-12 months",
    "over 12 months",
    "contract_number",
    "customer_name",
    "expire_date",
    "number_of_vehicles",
    "remaining_days",
    "desc",
    "asc",
]


def validate_array_data(data):
    if data not in array_data:
        raise ValueError(f"Invalid value: {data}")
    return data


def check_role_supervisor(current_user):
    roles = current_user.role_name
    if not roles:
        roles = []
    return (
        "SCG-Inter Administrator" in roles
        or "SCG-Inter Fleet Manager" in roles
        or "System Manager" in roles
    )


today = datetime.today()
next_three_months = datetime.today() + relativedelta(months=3)
next_six_months = datetime.today() + relativedelta(months=6)
next_twelve_months = datetime.today() + relativedelta(months=12)


def get_date_from_period(expire_period):
    if expire_period == "0-3 months":
        return today, next_three_months
    if expire_period == "3-6 months":
        return next_three_months, next_six_months
    if expire_period == "6-12 months":
        return next_six_months, next_twelve_months


def get_company_name_from_user(current_user: User, db):
    company_name_list = (
        db.query(Company.name)
        .join(Customer)
        .filter(
            Company.id == Customer.company_id,
            Customer.system_user == current_user.username,
        )
        .all()
    )
    if company_name_list is None:
        return []
    else:
        return company_name_list
