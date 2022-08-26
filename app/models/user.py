from sqlalchemy import DATETIME, Column, Integer, String

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
    creation = Column(DATETIME)
    modified = Column(DATETIME)
    owner = Column(String(255))
    role_name = Column(String(100))
