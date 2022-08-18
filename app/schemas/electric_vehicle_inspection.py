from pydantic import BaseModel


class VehicleInspectionBase(BaseModel):
    id: str = None
    creation: str = None
    modified: str = None
    modified_by: str = None
    owner: str = None


class VehicleInspectionResponse(VehicleInspectionBase):
    """This the serializer exposed on the API"""

    pass


class VehicleInspectionCreate(VehicleInspectionBase):
    """This is the serializer used for POST/PATCH requests"""

    pass
