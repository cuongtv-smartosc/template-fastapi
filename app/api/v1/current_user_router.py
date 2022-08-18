from fastapi import Depends
from fastapi.routing import APIRouter

from app.models.user import User
from app.schemas.response import resp
from app.services.auth import get_current_user

current_user_router = APIRouter()


@current_user_router.get("/")
async def get_current_user(
    current_user: User = Depends(get_current_user),
):
    """
    This endpoint get authenticated user.
    """
    return resp.success(data=current_user)
