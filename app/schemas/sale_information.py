from pydantic import BaseModel, conint, constr, validator

from app.common.util import validate_array_data
from app.schemas.base import BaseModelSchemas


class SaleInformationBase(BaseModelSchemas):
    id: str = None


class SaleInformationResponse(SaleInformationBase):
    """This the serializer exposed on the API"""

    pass


class SaleInformationCreate(SaleInformationBase):
    """This is the serializer used for POST/PATCH requests"""

    pass


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
    def unique_check_expire_period(cls, v):
        return validate_array_data(v)

    @validator("sort_by")
    def unique_check_sort_by(cls, v):
        return validate_array_data(v)

    @validator("sort_order")
    def unique_check_sort_order(cls, v):
        return validate_array_data(v)
