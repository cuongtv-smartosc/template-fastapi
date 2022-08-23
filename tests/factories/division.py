import factory.fuzzy

from app.models.division import Division
from tests.base_test import SessionTest


class DivisionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Division
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = "zoneA"
    name = "zone A"
