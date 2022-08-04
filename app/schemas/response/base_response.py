from typing import Generic, TypeVar, Optional, List

from pydantic import BaseModel, validator, ValidationError
from pydantic.generics import GenericModel

# T = TypeVar('T')  # Can be anything
# A = TypeVar('A', str, bytes)  # Must be str or bytes
DataT = TypeVar('DataT')


class Error(BaseModel):
    code: int
    message: str


class Response(GenericModel, Generic[DataT]):
    data: Optional[DataT]
    error: Optional[Error]

    @validator('error', always=True)
    def check_consistency(cls, v, values):
        if v is not None and values['data'] is not None:
            raise ValueError('must not provide both data and error')
        if v is None and values.get('data') is None:
            raise ValueError('must provide data or error')
        return v
