from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.models.user import User
from app.schemas.response import resp
from app.services.auth import get_current_user
from app.services.overview_page import pdi_status_chart

pdi_status_chart_router = APIRouter()


@pdi_status_chart_router.get("/")
def pdi_status_charts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    chart = pdi_status_chart(db, current_user)
    return resp.success(data=chart)
