import factory.fuzzy

from app.models.charger import Charger
from tests.base_test import SessionTest


class ChargerFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Charger
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    model = "1"
