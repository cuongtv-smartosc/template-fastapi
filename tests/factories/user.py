import factory.fuzzy

from app.common.database import SessionLocal
from app.models.user import User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"

    username = "admin"
    role_name = "SCG-Inter Administrator"
