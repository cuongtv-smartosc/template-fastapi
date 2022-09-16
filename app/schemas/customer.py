from app.schemas.base import BaseModelSchemas, BaseModelUpdate


class CusTomerBase(BaseModelSchemas):
    customer_name: str = None
    address: str = None


class CusTomerResponse(CusTomerBase):
    """This the serializer exposed on the API"""

    pass


class CustomerCreate(CusTomerBase):
    """This is the serializer used for POST/PATCH requests"""

    pass


class CustomerUpdate(BaseModelUpdate):
    customer_name: str = None
    address: str = None
