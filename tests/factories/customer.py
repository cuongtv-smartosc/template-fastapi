import factory.fuzzy
from factory import LazyAttribute

from app.models.customer import Customer
from tests.base_test import SessionTest
from tests.factories.company import CompanyFactory


class CustomerFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Customer
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    customer_name = factory.fuzzy.FuzzyText("customer_name")
    company_id = LazyAttribute(lambda a: CompanyFactory().id)
