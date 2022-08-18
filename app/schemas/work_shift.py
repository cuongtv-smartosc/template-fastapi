from app.schemas.base import BaseModelSchemas


class WorkShiftBase(BaseModelSchemas):
    id: str = None


class WorkShiftResponse(WorkShiftBase):
    """This the serializer exposed on the API"""

    pass


class WorkShiftCreate(WorkShiftBase):
    """This is the serializer used for POST/PATCH requests"""

    pass