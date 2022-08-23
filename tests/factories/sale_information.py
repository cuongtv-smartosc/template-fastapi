import factory.fuzzy

from app.models.sale_information import SaleInformation
from tests.base_test import SessionTest


class SaleInformationFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = SaleInformation
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = "00009"
    sale_type = "inventory_new"
    sale_order_number = "00009"
    end_date = "2022-11-01"
    customer_id = "222"
