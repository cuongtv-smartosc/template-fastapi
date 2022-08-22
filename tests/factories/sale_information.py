import factory.fuzzy

from app.models.sale_information import SaleInformation
from tests.base_test import SessionTest


class SaleInformationFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = SaleInformation
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = factory.fuzzy.FuzzyText("id")
    sale_type = "inventory_new"
