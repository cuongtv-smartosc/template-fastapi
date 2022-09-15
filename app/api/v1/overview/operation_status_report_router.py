from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.models.user import User
from app.schemas.response import resp
from app.services.auth import get_current_user
from app.services.overview_page import operation_status_report

operation_status_report_router = APIRouter()


@operation_status_report_router.get("/")
def operation_status_reports(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    chart = operation_status_report(db, current_user)
    return resp.success(data=chart)
