import factory.fuzzy

from app.common.database import SessionLocal
from app.models.work_shift import WorkShift


class WorkShiftFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = WorkShift
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"
