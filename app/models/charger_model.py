from datetime import datetime

from sqlalchemy import Column, DateTime, String

from app.common.database import DBBaseCustom


class ChargerModel(DBBaseCustom):
    __tablename__ = "tabCharger Model"
    name = Column(String(255), unique=True, index=True, primary_key=True)
    model = Column(String(255))
    creation = Column(DateTime, nullable=False, default=datetime.utcnow())
    modified = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )
