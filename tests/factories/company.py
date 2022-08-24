import factory.fuzzy

from app.models.company import Company
from tests.base_test import SessionTest


class CompanyFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Company
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = factory.Sequence(lambda n: "111-%04d" % n)
