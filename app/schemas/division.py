from app.schemas.base import BaseModelSchemas


class DivisionBase(BaseModelSchemas):
    id: str = None
    division_name: str = None


# Properties to receive on item creation
class DivisionCreate(DivisionBase):
    pass


# Properties to return to client
class DivisionResponse(DivisionBase):
    """This the serializer exposed on the API"""

    pass
