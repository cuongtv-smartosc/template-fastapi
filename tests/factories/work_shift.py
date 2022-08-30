import factory.fuzzy

from app.models.work_shift import WorkShift
from tests.base_test import SessionTest


class DivisionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = WorkShift
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"
