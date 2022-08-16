from pydantic import BaseModel


class WorkShiftBase(BaseModel):
    name: str = None
    description: None | str = None
    creation: str = None
    modified: str = None
    modified_by: str = None
    owner: str = None


class WorkShiftResponse(WorkShiftBase):
    """This the serializer exposed on the API"""

    pass


class WorkShiftCreate(WorkShiftBase):
    """This is the serializer used for POST/PATCH requests"""

    pass
