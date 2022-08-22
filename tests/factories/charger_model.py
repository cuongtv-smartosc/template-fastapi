import factory.fuzzy

from app.models.charger_model import ChargerModel
from tests.base_test import SessionTest


class ChargerModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = ChargerModel
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = "1"
    name = factory.Faker("name")
