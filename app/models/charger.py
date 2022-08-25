from datetime import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.common.database import DBBaseCustom
from app.models.charger_model import ChargerModel


class Charger(DBBaseCustom):
    __tablename__ = "charger"
    id = Column(
        Integer,
        unique=True,
        index=True,
        primary_key=True,
        autoincrement=True,
    )
    creation = Column(DateTime, nullable=False, default=datetime.utcnow())
    modified = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )
    modified_by = Column(String(255))
    owner = Column(String(255))
    manufactoring_date = Column(Date)
    serial_number = Column(String(255))
    model = Column(Integer, ForeignKey(ChargerModel.id))
    import_date = Column(DateTime)
    charger_pdi_status = Column(String(255))
    charger_model = relationship("ChargerModel", back_populates="charger")
