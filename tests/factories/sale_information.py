import datetime
import random

import factory.fuzzy

from app.models.sale_information import SaleInformation
from tests.base_test import SessionTest


class SaleInformationFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = SaleInformation
        sqlalchemy_session = SessionTest()
        sqlalchemy_session_persistence = "commit"

    id = factory.Sequence(lambda n: "113-%04d" % n)
    sale_type = factory.Iterator(
        ["rent", "sold", "inventory_used", "inventory_new"],
    )
    sale_order_number = factory.fuzzy.FuzzyText("sale_order_number")
    end_date = factory.fuzzy.FuzzyDate(
        datetime.date(random.randint(2021, 2022), random.randint(1, 7), 1),
    )
    customer_id = factory.Sequence(lambda n: "112-%04d" % n)
