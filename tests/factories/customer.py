import factory.fuzzy

from app.models.customer import Customer
from tests.base_test import SessionTest


class CustomerFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Customer
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = factory.fuzzy.FuzzyText("id")
    customer_name = factory.fuzzy.FuzzyText("customer_name")
