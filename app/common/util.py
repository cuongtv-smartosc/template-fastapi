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
