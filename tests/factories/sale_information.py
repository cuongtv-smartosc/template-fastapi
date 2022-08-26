import factory.fuzzy

from app.models.sale_information import SaleInformation
from tests.base_test import SessionTest


class SaleInformationFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = SaleInformation
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    sale_type = factory.fuzzy.FuzzyText("id")
    customer_id = "customer_id"
