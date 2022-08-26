from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.common.database import DBBaseCustom


class User(DBBaseCustom):
    """This is an example model for your application.
    Replace with the *things* you do in your application.
    """

    __tablename__ = "user"
    id = Column(
        Integer,
        unique=True,
        index=True,
        primary_key=True,
        autoincrement=True,
    )
    username = Column(String(255), unique=True, index=True)
    hash_password = Column(String(255))
    creation = Column(DateTime, nullable=False, default=datetime.utcnow())
    modified = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )
    modified_by = Column(String(255))
    owner = Column(String(255))
    role_name = Column(String(100))
