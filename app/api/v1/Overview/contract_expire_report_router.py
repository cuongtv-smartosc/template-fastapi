from fastapi import APIRouter, Depends
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.common.handle_error import ValidateException
from app.models.user import User
from app.schemas.response import resp
from app.schemas.sale_information import SaleInformationFilter
from app.schemas.sale_information import SaleInformationGet as SaleInforGet
from app.services.auth import get_current_user
from app.services.overview_page import contract_expire_report

contract_expire_router = APIRouter()


@contract_expire_router.get("/")
def contract_expire_reports(
    params: SaleInforGet = Depends(),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        filters = params.__dict__
        page = filters.get("page")
        number_of_record = filters.get("number_of_record")

        filters = SaleInformationFilter(**filters).dict()

        expire_period = filters.get("expire_period")
        sort_by = filters.get("sort_by")
        sort_order = filters.get("sort_order")

        data = contract_expire_report(
            page,
            number_of_record,
            expire_period,
            sort_by,
            sort_order,
            db,
            current_user,
        )
        return resp.success(data=data)
    except ValidationError as e:
        raise ValidateException(e.errors())
