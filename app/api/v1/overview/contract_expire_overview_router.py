from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.models.user import User
from app.schemas.response import resp
from app.services.auth import get_current_user
from app.services.overview_page import contract_expire_overview_report

contract_expire_overview_router = APIRouter()


@contract_expire_overview_router.get("/")
def contract_expire_reports(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    data = contract_expire_overview_report(db, current_user)
    return resp.success(data=data)
