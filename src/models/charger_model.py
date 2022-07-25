from typing import Union

from peewee import CharField
from pydantic import BaseModel
from src.models.base_model import BaseModelPeewee, paginator


class ChargerModel(BaseModelPeewee):
    """This is an example model for your application.
    Replace with the *things* you do in your application.
    """

    name = CharField(primary_key=True)
    model = CharField()

    class Meta:
        table_name = 'tabCharger Model'

    @classmethod
    def fetch_all(cls, page: int = 1, page_size: int = 10):
        db = ChargerModel.select()
        data_list, paginate = paginator(db, page, page_size, "name desc")
        return data_list, paginate


class ChargerResponse(BaseModel):
    """This the serializer exposed on the API"""

    name: str
    model: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ChargerIncoming(BaseModel):
    """This is the serializer used for POST/PATCH requests"""

    name: Union[str, None] = None
    model: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
