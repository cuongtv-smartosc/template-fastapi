import factory.fuzzy

from app.models.charger import Charger
from app.models.charger_model import ChargerModel
from tests.base_test import SessionTest


class ChargerFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Charger
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = factory.fuzzy.FuzzyText("id")
