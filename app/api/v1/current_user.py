from fastapi import Depends
from fastapi.routing import APIRouter

from app.models.user_model import UserModel
from app.services.auth import get_current_user

user = APIRouter()


@user.get("/")
async def get_list_models(current_user: UserModel = Depends(get_current_user)):
    return current_user
