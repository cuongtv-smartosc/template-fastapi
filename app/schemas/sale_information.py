
from app.schemas.base import BaseModelSchemas


class SaleInformationBase(BaseModelSchemas):
    id: str = None


class SaleInformationResponse(SaleInformationBase):
    """This the serializer exposed on the API"""

    pass


class SaleInformationCreate(SaleInformationBase):
    """This is the serializer used for POST/PATCH requests"""

    pass