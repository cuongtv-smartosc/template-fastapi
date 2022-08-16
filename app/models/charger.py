from datetime import datetime

from sqlalchemy import Column, DateTime, String

from app.common.database import DBBaseCustom


class Charger(DBBaseCustom):
    __tablename__ = "tabCharger"
    name = Column(String(255), unique=True, index=True, primary_key=True)
    creation = Column(DateTime, nullable=False, default=datetime.utcnow())
    modified = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )
    modified_by = Column(String(255))
    owner = Column(String(255))
    serial_number = Column(String(255))
    model = Column(String(255))
    import_date = Column(DateTime)
    charger_pdi_status = Column(DateTime)
