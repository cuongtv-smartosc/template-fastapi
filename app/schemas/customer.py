from app.schemas.base import BaseModelSchemas


class CusTomerBase(BaseModelSchemas):
    id: str = None


class CusTomerResponse(CusTomerBase):
    """This the serializer exposed on the API"""

    pass


class CustomerCreate(CusTomerBase):
    """This is the serializer used for POST/PATCH requests"""

    pass
