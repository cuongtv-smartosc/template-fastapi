from pydantic import BaseModel, conint, constr, validator
from pydantic.schema import date

from app.common.util import validate_unique_for_update
from app.models.customer import Customer
from app.models.sale_information import SaleInformation
from app.schemas.base import BaseModelSchemas, BaseModelUpdate


class SaleInformationBase(BaseModelSchemas):
    id: int = None
    sale_order_number: str = None
    sale_type: str = None
    start_date: date = None
    end_date: date = None
    vehicle_warranty: int = None
    battery_warranty: int = None
    battery_maintenance: int = None
    location: str = None
    service: str = None
    product_number: str = None
    working_days: str = None
    customer_id: int = None


class SaleInformationResponse(SaleInformationBase):
    """This the serializer exposed on the API"""

    pass


class SaleInformationCreate(SaleInformationBase):
    """This is the serializer used for POST/PATCH requests"""

    customer_name: str = None
    address: str = None
    delivering_date: date = None


class SaleInformationGet(BaseModel):
    page: conint(ge=0) | None = 0
    number_of_record: conint(ge=1) | None = 5
    expire_period: constr(min_length=10, max_length=14) | None = "0-3 months"
    sort_by: constr(min_length=11, max_length=18) | None = "remaining_days"
    sort_order: constr(min_length=3, max_length=4) | None = "asc"


class SaleInformationFilter(BaseModel):
    expire_period: str
    sort_by: str
    sort_order: str

    @validator("expire_period")
    def unique_check_expire_period(cls, expire_period):
        if expire_period not in [
            "0-3 months",
            "3-6 months",
            "6-12 months",
            "over 12 months",
        ]:
            raise ValueError(f"Invalid value: {expire_period}")
        return expire_period

    @validator("sort_by")
    def unique_check_sort_by(cls, sort_by):
        if sort_by not in [
            "contract_number",
            "customer_name",
            "expire_date",
            "number_of_vehicles",
            "remaining_days",
        ]:
            raise ValueError(f"Invalid value: {sort_by}")
        return sort_by

    @validator("sort_order")
    def unique_check_sort_order(cls, sort_order):
        if sort_order not in ["desc", "asc"]:
            raise ValueError(f"Invalid value: {sort_order}")
        return sort_order


class SaleInformationUpdate(BaseModelUpdate):
    id: int = None
    sale_order_number: str = None
    sale_type: str = None
    start_date: date = None
    end_date: date = None
    vehicle_warranty: int = None
    battery_warranty: int = None
    battery_maintenance: int = None
    location: str = None
    service: str = None
    product_number: str = None
    working_days: str = None
    customer_id: int = None
    customer_name: str = None
    address: str = None
    delivering_date: date = None

    @validator("sale_order_number")
    def unique_check_sale_order_number(cls, value, values):
        return validate_unique_for_update(
            SaleInformation,
            "sale_order_number",
            values["id"],
            sale_order_number=value,
        )

    @validator("customer_name")
    def unique_check_customer_name(cls, value, values):
        return validate_unique_for_update(
            Customer,
            "customer_name",
            values["customer_id"],
            customer_name=value,
        )
