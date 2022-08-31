from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.schemas.response import resp
from app.services.overview_page import sale_type_stat

sale_type_stats_router = APIRouter()


@sale_type_stats_router.get("/")
def sale_type_stats(db: Session = Depends(get_db)):
    chart = sale_type_stat(db)
    return resp.success(data=chart)
