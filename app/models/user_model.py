from app.db.config_db_sqlalchemy import DBBaseCustom
from sqlalchemy import Column, String

# class UserModel(DBBaseCustom):
#     """This is an example model for your application.
#     Replace with the *things* you do in your application.
#     """
#
#     __tablename__ = "tabUser"


users_db = {
    "linh": {
        "username": "linh",
        "full_name": "Linh Vu",
        "hash_password": "1",
    },
    "mai": {
        "username": "mai",
        "full_name": "Huyen Mai",
        "hash_password": "2",
    },
}
