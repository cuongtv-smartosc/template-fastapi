from pydantic import BaseModel, conint, constr

from app.schemas.base import BaseModelSchemas


class VehicleHistoryBase(BaseModelSchemas):
    id: str = None


class VehicleHistoryResponse(VehicleHistoryBase):
    """This the serializer exposed on the API"""

    pass


class VehicleHistoryCreate(VehicleHistoryBase):
    """This is the serializer used for POST/PATCH requests"""

    pass


class VehicleHistoryGet(BaseModel):
    status: constr(min_length=0) | None = ""
    page_size: conint(ge=1) | None = 10
    current_page: conint(ge=1) | None = 1
