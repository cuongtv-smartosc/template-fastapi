from app.schemas.base import BaseModelSchemas


class VehicleHistoryBase(BaseModelSchemas):
    id: str = None


class VehicleHistoryResponse(VehicleHistoryBase):
    """This the serializer exposed on the API"""

    pass


class VehicleHistoryCreate(VehicleHistoryBase):
    """This is the serializer used for POST/PATCH requests"""

    pass