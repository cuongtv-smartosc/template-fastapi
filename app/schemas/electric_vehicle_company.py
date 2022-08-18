from pydantic import BaseModel


class VehicleCompanyBase(BaseModel):
    id: str = None
    creation: str = None
    modified: str = None
    modified_by: str = None
    owner: str = None


class VehicleCompanyResponse(VehicleCompanyBase):
    """This the serializer exposed on the API"""

    pass


class VehicleCompanyCreate(VehicleCompanyBase):
    """This is the serializer used for POST/PATCH requests"""

    pass
