import json

from pydantic import BaseModel, conint, constr, validator
from pydantic.schema import date

from app.schemas.base import BaseModelSchemas, BaseModelUpdate


class VehicleBase(BaseModelSchemas):
    delivering_date: date = None


class VehicleResponse(VehicleBase):
    """This the serializer exposed on the API"""

    vehicle_number: str = None
    model_id: str = None
    edge_id: str = None
    customer_id: str = None
    operation_status: str = None


class VehicleCreate(VehicleBase):
    """This is the serializer used for POST/PATCH requests"""

    pass


class VehicleGetListParams(BaseModel):
    page_size: conint(ge=1) | None = None
    current_page: conint(ge=1) | None = None
    order_by: constr(min_length=1, max_length=255) | None = None
    company_name: constr(min_length=1) | None = None
    customer_name: constr(min_length=1) | None = None
    division_name: constr(min_length=1) | None = None
    work_shift: constr(min_length=1) | None = None
    model_id: constr(min_length=1) | None = None
    vehicle_number: constr(min_length=1) | None = None
    operation_status: constr(min_length=1) | None = None
    sale_id: constr(min_length=1) | None = None
    sale_type: constr(min_length=1) | None = None
    location: constr(min_length=1) | None = None
    forklift_pdi_status: constr(min_length=1) | None = None
    sale_order_number: constr(min_length=1) | None = None
    period: constr(min_length=1) | None = None
    offset: constr(min_length=1) | None = None
    page: conint(ge=0) | None = 0
    number_of_record: conint(ge=1) | None = 5
    sort_by: constr(min_length=8, max_length=18) | None = "number_of_vehicles"
    sort_order: constr(min_length=3, max_length=4) | None = "desc"


class VehicleGetListFilterList(BaseModel):
    company_name: str = None
    customer_name: str = None
    division_name: str = None
    work_shift: str = None
    model_id: str = None
    vehicle_number: str = None
    operation_status: str = None

    @validator(
        "customer_name",
        "company_name",
        "division_name",
        "work_shift",
        "model_id",
        "vehicle_number",
        "operation_status",
    )
    def check_type(cls, v):
        try:
            if v:
                data = json.loads(v)
                if not isinstance(data, list):
                    raise ValueError("value is not a valid list")
        except Exception:
            raise ValueError("value is not a valid list")
        return v


class VehicleGetListFilterString(BaseModel):
    sale_id: str = None
    sale_type: str = None
    location: str = None
    forklift_pdi_status: str = None
    sale_order_number: str = None
    period: str = None
    offset: str = None
    sort_by: str = None
    sort_order: str = None

    @validator("sort_by")
    def unique_check_sort_by(cls, sort_by):
        if sort_by not in ["number_of_vehicles", "location"]:
            raise ValueError(f"Invalid value: {sort_by}")
        return sort_by

    @validator("sort_order")
    def unique_check_sort_order(cls, sort_order):
        if sort_order not in ["asc", "desc"]:
            raise ValueError(f"Invalid value: {sort_order}")
        return sort_order


class VehicleUpdate(BaseModelUpdate):
    delivering_date: date = None
