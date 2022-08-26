import factory.fuzzy

from app.models.customer import Customer
from tests.base_test import SessionTest


class CustomerFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Customer
        sqlalchemy_session_persistence = "commit"
        sqlalchemy_session = SessionTest()

    customer_name = factory.fuzzy.FuzzyText("customer_name")
    company_id = "1"
