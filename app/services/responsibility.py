from fastapi.encoders import jsonable_encoder

from app.common.handle_error import NotFoundException
from app.models.division import Division
from app.models.electric_vehicle_divison import VehicleDivision
from app.models.work_shift import WorkShift
from app.services.electric_vehicle import get_by_id


def get_responsibility(vehicle_id, db, current_user):
    vehicle = get_by_id(vehicle_id, db, current_user)
    if not vehicle:
        raise NotFoundException(f"{vehicle_id} is not existed")
    div = (
        db.query(VehicleDivision.id, Division.name)
        .filter(
            VehicleDivision.division_id == Division.id,
            VehicleDivision.vehicle_id == vehicle_id,
        )
        .all()
    )
    work_shift = (
        db.query(
            WorkShift.id,
            WorkShift.workings_day,
            WorkShift.work_shift,
            WorkShift.work_shift_from,
            WorkShift.work_shift_to,
        )
        .filter(WorkShift.vehicle_id == vehicle_id)
        .all()
    )
    div = jsonable_encoder(div)
    work_shift = jsonable_encoder(work_shift)
    return {"zone": div, "workShift": work_shift}
