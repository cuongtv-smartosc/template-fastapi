from datetime import datetime

from pydantic import validator

from app.schemas.base import BaseModelSchemas, BaseModelUpdate


class ChargerBase(BaseModelSchemas):
    id: str = None


# Properties to receive on item creation
class ChargerCreate(ChargerBase):
    pass


# Properties to return to client
class ChargerResponse(ChargerBase):
    """This the serializer exposed on the API"""

    pass


class ChargerUpdate(BaseModelUpdate):
    manufactoring_date: str = None

    @validator(
        "manufactoring_date",
    )
    def validate_date_type(
        cls,
        value,
    ):
        if value:
            try:
                value = datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                raise ValueError("invalid date format")
        return value
