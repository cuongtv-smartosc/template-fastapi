import math

from fastapi.encoders import jsonable_encoder

from app.common.handle_error import NotFoundException
from app.models.electric_vehicle_history import VehicleHistory
from app.services.electric_vehicle import get_by_id


def get_list_status(
    vehicle_id,
    current_page,
    page_size,
    filters,
    db,
    current_user,
):
    vehicle = get_by_id(vehicle_id, db, current_user)
    if not vehicle:
        raise NotFoundException(f"{vehicle_id} is not existed")
    offset = (current_page - 1) * page_size
    query = db.query(
        VehicleHistory.id,
        VehicleHistory.status,
        VehicleHistory.detail,
        VehicleHistory.update_by,
        VehicleHistory.update_time,
    ).filter(VehicleHistory.vehicle_id == vehicle_id)
    if filters:
        query = query.filter(VehicleHistory.status == filters)
    status = jsonable_encoder(
        query.order_by(VehicleHistory.update_time.desc())
        .limit(page_size)
        .offset(offset)
        .all()
    )
    total_status = query.count()
    total_page = math.ceil(total_status / page_size)
    return {
        "total": total_status,
        "currentPage": current_page,
        "totalPage": total_page,
        "data": status,
    }
