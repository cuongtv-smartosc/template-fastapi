from fastapi.routing import APIRouter
from app.schemas.item_model import ItemModel
from pydantic import ValidationError
from app.schemas.response.base_response import Response, Error

router_index = APIRouter()

items = [
    {"name": "Foo", "price": 50.2},
    {"name": "Bar", "description": "The bartenders", "price": 62},
    {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5},
]

@router_index.get("/items/{item_id}")
async def read_item(item_id: int):
    try:
        if item_id > 2:
            error = Error(code=404, message='Not found')
            return Response[ItemModel](error=error)
        return Response[ItemModel](data=items[item_id])
    except ValidationError as e:
        print('error here', e)

