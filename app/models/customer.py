from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.common.database import DBBaseCustom


class Customer(DBBaseCustom):
    __tablename__ = "customer"
    id = Column(
        Integer,
        unique=True,
        index=True,
        primary_key=True,
        autoincrement=True,
    )
    creation = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )
    modified = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )
    modified_by = Column(String(255))
    owner = Column(String(255))
    customer_name = Column(String(255))
    address = Column(String(255))
    company_id = Column(Integer, ForeignKey("company.id"))
    system_user = Column(String(255))
    sale_information = relationship("SaleInformation", backref="customer")
