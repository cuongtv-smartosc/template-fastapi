from pydantic import BaseModel


class SaleInformationBase(BaseModel):
    id: str = None
    creation: str = None
    modified: str = None
    modified_by: str = None
    owner: str = None


class SaleInformationResponse(SaleInformationBase):
    """This the serializer exposed on the API"""

    pass


class SaleInformationCreate(SaleInformationBase):
    """This is the serializer used for POST/PATCH requests"""

    pass
