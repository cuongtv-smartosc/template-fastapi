import json

from pydantic import BaseModel, conint, constr, validator

from app.schemas.base import BaseModelSchemas


class VehicleBase(BaseModelSchemas):
    id: str = None


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


class VehicleGet(BaseModel):
    page_size: conint(ge=1)
    current_page: conint(ge=1)
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


class VehicleFilterList(BaseModel):
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


class VehicleFilter(BaseModel):
    sale_id: str = None
    sale_type: str = None
    location: str = None
    forklift_pdi_status: str = None
    sale_order_number: str = None
    period: str = None
    offset: str = None
