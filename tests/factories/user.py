import factory.fuzzy

from app.models.user import User
from tests.base_test import SessionTest


class DivisionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    username = "admin"
    role_name = "SCG-Inter Administrator"
