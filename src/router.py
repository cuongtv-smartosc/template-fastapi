from fastapi import APIRouter

import settings
from src.routers.charger_model_router import charger_model_router
from src.routers.index import router_index
from src.routers.vehicle_model_router import vehicle_model

router = APIRouter()

# router index
router.include_router(router_index, prefix=f"{settings.API_PREFIX}")

# router charger model
router.include_router(charger_model_router, prefix=f"{settings.API_PREFIX}/charger-model")

# router vehicle model
router.include_router(vehicle_model, prefix=f"{settings.API_PREFIX}")