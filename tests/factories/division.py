import factory.fuzzy

from app.common.database import SessionLocal
from app.models.division import Division


class DivisionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Division
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"
