from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.common.database import get_db
from app.schemas.response import resp
from app.services.overview_page import pdi_status_chart

pdi_status_chart_router = APIRouter()


@pdi_status_chart_router.get("/")
def pdi_status_charts(db: Session = Depends(get_db)):
    chart = pdi_status_chart(db)
    return resp.success(data=chart)
