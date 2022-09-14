import factory.fuzzy
from factory import LazyAttribute

from app.common.database import SessionLocal
from app.models.customer import Customer
from tests.factories.company import CompanyFactory


class CustomerFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Customer
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"

    customer_name = factory.fuzzy.FuzzyText("customer_name")
    company_id = LazyAttribute(lambda a: CompanyFactory().id)
    system_user = factory.fuzzy.FuzzyText("name")
