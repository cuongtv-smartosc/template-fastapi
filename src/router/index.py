from fastapi.routing import APIRouter

from src.schemas.response import resp

router = APIRouter()


@router.get("/")
async def index():
    return resp.success(data="Hello World")
