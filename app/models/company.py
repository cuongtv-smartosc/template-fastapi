from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.common.database import DBBaseCustom


class Company(DBBaseCustom):
    __tablename__ = "company"
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
    name = Column(String(255))
