from pydantic import BaseModel


class VehicleCusTomerBase(BaseModel):
    name: str = None
    description: None | str = None
    creation: str = None
    modified: str = None
    modified_by: str = None
    owner: str = None


class VehicleCusTomerResponse(VehicleCusTomerBase):
    """This the serializer exposed on the API"""

    pass


class VehicleCustomerCreate(VehicleCusTomerBase):
    """This is the serializer used for POST/PATCH requests"""

    pass
