from pydantic import validator

from app.common.util import validate_unique_for_update
from app.models.customer import Customer
from app.schemas.base import BaseModelSchemas, BaseModelUpdate


class CusTomerBase(BaseModelSchemas):
    customer_name: str = None
    address: str = None


class CusTomerResponse(CusTomerBase):
    """This the serializer exposed on the API"""

    pass


class CustomerCreate(CusTomerBase):
    """This is the serializer used for POST/PATCH requests"""

    pass


class CustomerUpdate(BaseModelUpdate):
    customer_id: int = None
    customer_name: str = None
    address: str = None

    @validator("customer_name")
    def unique_check_customer_name(cls, value, values):
        return validate_unique_for_update(
            Customer,
            "customer_name",
            values["customer_id"],
            customer_name=value,
        )
