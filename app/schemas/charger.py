from app.schemas.base import BaseModelSchemas


class ChargerBase(BaseModelSchemas):
    id: str = None


# Properties to receive on item creation
class ChargerCreate(ChargerBase):
    pass


# Properties to return to client
class ChargerResponse(ChargerBase):
    """This the serializer exposed on the API"""

    pass