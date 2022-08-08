from app.api.auth_v1.auth import auth_jwt
from fastapi import APIRouter
from app.api.v1.current_user import user
from app.api.v1.charger_model_router import charger_model_router
from app.api.v1.index import router_index
from app.api.v1.vehicle_model_router import vehicle_model
from app.config import settings

api_v1_router = APIRouter()

# router index
api_v1_router.include_router(router_index, prefix=f"{settings.API_PREFIX}")

# router charger model
api_v1_router.include_router(
    charger_model_router, prefix=f"{settings.API_PREFIX}/charger-model"
)

# router vehicle model
api_v1_router.include_router(
    vehicle_model, prefix=f"{settings.API_PREFIX}/vehicle-model"
)
api_v1_router.include_router(auth_jwt, prefix=f"{settings.API_PREFIX}/auth")

api_v1_router.include_router(
    user,
    prefix=f"{settings.API_PREFIX}/get_current_user",
)
