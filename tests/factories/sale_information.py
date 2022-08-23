import factory.fuzzy

from app.models.sale_information import SaleInformation
from tests.base_test import SessionTest


class SaleInformationFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = SaleInformation
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = "S1"
    sale_type = "1"
    customer_id = "C1"
