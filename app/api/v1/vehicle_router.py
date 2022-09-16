import json
from datetime import datetime

from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRouter
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.common.handle_error import ValidateException
from app.models.user import User
from app.schemas.customer import CustomerUpdate
from app.schemas.electric_vehicle import (
    VehicleGetListFilterList,
    VehicleGetListFilterString,
    VehicleGetListParams,
    VehicleUpdate,
)
from app.schemas.electric_vehicle_history import VehicleHistoryGet
from app.schemas.response import resp
from app.schemas.sale_information import SaleInformationCreate
from app.schemas.sale_information import SaleInformationUpdate as SaleUpdate
from app.services.auth import get_current_user
from app.services.electric_vehicle import get_detail, get_vehicle_list
from app.services.responsibility import get_responsibility
from app.services.sale_information import (
    get_sale_information,
    update_sale_information_detail,
)
from app.services.vehicle_history import get_list_status

vehicle_router = APIRouter()


@vehicle_router.get("/")
async def get_vehicles(
    params: VehicleGetListParams = Depends(),
    current_user: User = Depends(
        get_current_user,
    ),
    db: Session = Depends(get_db),
):
    try:
        filters = jsonable_encoder(params)
        filter = VehicleGetListFilterList(**filters).dict()
        for key in filter:
            if filter[key] is not None:
                filter[key] = json.loads(filter[key])
        filter.update(VehicleGetListFilterString(**filters).dict())
        results = get_vehicle_list(
            filters=filter,
            current_page=params.current_page,
            page_size=params.page_size,
            order_by=params.order_by,
            db=db,
            current_user=current_user,
        )
        return resp.success(data=results)
    except ValidationError as e:
        raise ValidateException(e.errors())


@vehicle_router.get("/{id}")
async def get_vehicle_detail(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    data = get_detail(id, db, current_user)
    return resp.success(data=data)


@vehicle_router.get("/{id}/sale_information")
async def get_sale_information_vehicle(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    sale_information = get_sale_information(id, db, current_user)
    return resp.success(data=sale_information)


@vehicle_router.get("/{id}/status")
async def get_status(
    id: int,
    params: VehicleHistoryGet = Depends(),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    current_page = params.current_page
    page_size = params.page_size
    filters = params.status
    status = get_list_status(
        id,
        current_page,
        page_size,
        filters,
        db,
        current_user,
    )
    return resp.success(data=status)


@vehicle_router.get("/{id}/responsibility")
async def get_responsibility_vehicle(
    id,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    data = get_responsibility(id, db, current_user)
    return resp.success(data=data)


@vehicle_router.patch("/{id}/sale_information")
async def update_sale_information(
    id: int,
    body_data: SaleInformationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        data = jsonable_encoder(body_data)
        data["modified"] = datetime.now().__str__()
        data["modified_by"] = current_user.username
        sale_information_body = SaleUpdate(**data).dict()
        vehicle_body = VehicleUpdate(**data).dict()
        customer_body = CustomerUpdate(**data).dict()
        vehicle_body.update()
        update_result = await update_sale_information_detail(
            id,
            db,
            sale_information_body,
            vehicle_body,
            customer_body,
        )
        return update_result
    except ValidationError as e:
        raise ValidateException(e.errors())
