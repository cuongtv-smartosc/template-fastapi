from pydantic import BaseModel, conint, constr, validator

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
