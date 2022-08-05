from fastapi.routing import APIRouter
from pydantic import BaseModel
from app.schemas.response import resp
from fastapi import Request, Response

router_index = APIRouter()



@router_index.get("/")
async def index():
    return resp.success(data="Hello World")


@router_index.get("/test_path_params/{item_id}")
def read_root(request: Request, item_id: str):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}


@router_index.get("/test_query_params")
def test(request: Request, a: int, b: int):

    return {"a": a, "b": b}


class Item(BaseModel):
    a: int
    b: int

@router_index.post("/test_body")
async def test_body(item: Item):

    return {"a": item.a, "b": item.b}


@router_index.post("/test_params_body")
async def test_body(item: Item, name: str):

    return {"a": item.a, "b": item.b, "name": name}
