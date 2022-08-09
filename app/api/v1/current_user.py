from fastapi import Depends
from fastapi.routing import APIRouter
from app.models.user import UserModel
from app.schemas.response import resp
from app.services.auth import get_current_user

current_user = APIRouter()


@current_user.get("/")
async def get_current_user(
    current_user: UserModel = Depends(get_current_user),
):
    return resp.success(data=current_user)


