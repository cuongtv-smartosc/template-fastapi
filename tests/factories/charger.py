import factory.fuzzy

from app.common.database import SessionLocal
from app.models.charger import Charger


class ChargerFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Charger
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"
