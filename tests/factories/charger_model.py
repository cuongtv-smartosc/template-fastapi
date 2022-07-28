from datetime import datetime

import factory.fuzzy

from src.db.config_db_sqlalchemy import ActiveSession
from src.models.charger_model import ChargerModel


class ChargerModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = ChargerModel
        sqlalchemy_session = ActiveSession
        sqlalchemy_session_persistence = "flush"

    name = "charger model test"
    model = "charger model test"
    creation = datetime.utcnow()
    owner = "SYSTEM"
    modified = datetime.utcnow()
    modified_by = "SYSTEM"
