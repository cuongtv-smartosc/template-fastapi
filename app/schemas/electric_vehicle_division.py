from app.schemas.base import BaseModelSchemas


class VehicleDivisionBase(BaseModelSchemas):
    id: str = None
    division_name: str = None


# Properties to receive on item creation
class VehicleDivisionCreate(VehicleDivisionBase):
    pass


# Properties to return to client
class VehicleDivisionResponse(VehicleDivisionBase):
    """This the serializer exposed on the API"""

    pass
