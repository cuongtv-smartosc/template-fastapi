from typing import List

from app.common.database import SessionLocal


def validate_unique(table, field, **kwargs):
    session = SessionLocal()
    q = session.query(getattr(table, field)).filter_by(**kwargs).scalar()
    session.close()
    if q:
        raise ValueError(f"""Table {table.__name__} {field} already exist""")
    return kwargs[field]


def is_invalid_order_by(order_by: str, fields: List[str] = []) -> bool:
    items = order_by.split()
    if len(items) != 2:
        return True

    if items[0] not in fields:
        return True

    return False
