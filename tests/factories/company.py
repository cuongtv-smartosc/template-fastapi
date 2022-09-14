import factory.fuzzy

from app.common.database import SessionLocal
from app.models.company import Company


class CompanyFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Company
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"

    name = factory.fuzzy.FuzzyText("name")
