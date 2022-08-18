from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.common.database import DBBaseCustom


class VehicleCompany(DBBaseCustom):
    __tablename__ = "tabElectric Vehicle Company"
    id = Column(String(255), unique=True, index=True, primary_key=True)
    creation = Column(DateTime,
                      nullable=False,
                      default=datetime.utcnow(), )
    modified = Column(DateTime,
                      nullable=False,
                      default=datetime.utcnow(),
                      onupdate=datetime.utcnow(), )
    modified_by = Column(String(255))
    owner = Column(String(255))
    company_name = Column(String(255))
