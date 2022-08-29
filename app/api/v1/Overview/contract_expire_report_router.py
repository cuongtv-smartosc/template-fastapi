from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.common.database import get_db
from app.schemas.response import resp
from app.services.over_view_page import contract_expire_report

contract_expire_router = APIRouter()


@contract_expire_router.get("/")
def contract_expire_reports(
    page=0,
    number_of_record=5,
    expire_period="0-3 months",
    sort_by="remaining_days",
    sort_order="asc",
    db: Session = Depends(get_db),
):
    data = contract_expire_report(
        page, number_of_record, expire_period, sort_by, sort_order, db
    )
    return resp.success(data=data)
