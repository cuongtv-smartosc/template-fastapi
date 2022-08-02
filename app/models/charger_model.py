from sqlalchemy import Column, String

from app.db.config_db_sqlalchemy import DBBaseCustom


class ChargerModel(DBBaseCustom):
    """This is an example model for your application.
    Replace with the *things* you do in your application.
    """

    __tablename__ = "tabCharger Model"
    name = Column(String(255), unique=True, index=True, primary_key=True)
    description = Column(String(255))