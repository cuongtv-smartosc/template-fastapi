from pydantic import BaseModel


class VehicleModelBase(BaseModel):
    name: str = None
    description: None | str = None


class VehicleModelResponse(VehicleModelBase):
    """This the serializer exposed on the API"""

    pass


class VehicleModelCreate(VehicleModelBase):
    """This is the serializer used for POST/PATCH requests"""

    pass
