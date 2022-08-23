import factory.fuzzy

from app.models.work_shift import WorkShift
from tests.base_test import SessionTest


class WorkShiftFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = WorkShift
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = "Ws1"
    vehicle_id = "1"
    work_shift_to = "20:00"
