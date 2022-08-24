import factory.fuzzy

from app.models.customer import Customer
from tests.base_test import SessionTest


class CustomerFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Customer
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = factory.Sequence(lambda n: "112-%04d" % n)
    customer_name = factory.fuzzy.FuzzyText("customer_name")
    company_id = factory.Sequence(lambda n: "111-%04d" % n)
