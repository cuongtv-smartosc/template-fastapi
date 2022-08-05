import factory.fuzzy

from app.common.database import SessionLocal
from app.models.charger_model import ChargerModel


class ChargerModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = ChargerModel
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"

    name = "charger model test"
    model = "charger model test"
