import random

import factory.fuzzy
from factory import LazyAttribute

from app.common.database import SessionLocal
from app.models.sale_information import SaleInformation
from tests.factories.customer import CustomerFactory


class SaleInformationFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = SaleInformation
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"

    sale_type = factory.fuzzy.FuzzyChoice(
        ["rent", "sold", "inventory_used", "inventory_new"],
    )
    sale_order_number = factory.fuzzy.FuzzyText("sale_order_number")
    end_date = f"2022-{random.randint(1, 2)}-1"
    customer_id = LazyAttribute(lambda a: CustomerFactory().id)
