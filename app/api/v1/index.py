from fastapi.routing import APIRouter

from app.schemas.response import resp

router_index = APIRouter()


@router_index.get("/")
async def index():
    return resp.success(data="Hello World")
