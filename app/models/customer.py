from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from app.common.database import DBBaseCustom
from app.models.company import Company


class Customer(DBBaseCustom):
    __tablename__ = "customer"
    id = Column(String(255), unique=True, index=True, primary_key=True)
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
    company_id = Column(String(255), ForeignKey(Company.id))
    system_user = Column(String(255))
    sale_information = relationship('SaleInformation', backref='customer', lazy=False)