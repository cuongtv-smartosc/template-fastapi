from fastapi import APIRouter

from app.api.endpoints import charger_model

api_router = APIRouter()
api_router.include_router(charger_model.router, prefix="/charger-model", tags=["charger-model"])
