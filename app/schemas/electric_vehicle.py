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
