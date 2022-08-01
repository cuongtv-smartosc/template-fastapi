from typing import Any, List

from fastapi import APIRouter, Depends

from app.schemas import ChargerModel

router = APIRouter()


@router.get("/", response_model=List[ChargerModel])
def read_items() -> Any:
    data = [
        {"name": "Charger Model 1"},
        {"name": "Charger Model 2"},
    ]
    return data
