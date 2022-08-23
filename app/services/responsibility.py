from fastapi.encoders import jsonable_encoder

from app.models.division import Division
from app.models.electric_vehicle_divison import VehicleDivision
from app.models.work_shift import WorkShift
from app.schemas.response import resp


def get_responsibility(id, db):
    query_div = (
        db.query(VehicleDivision.id, Division.name)
        .filter(
            VehicleDivision.division_id == Division.id,
            VehicleDivision.vehicle_id == id,
        )
        .all()
    )
    query_work_shift = (
        db.query(
            WorkShift.id,
            WorkShift.workings_day,
            WorkShift.work_shift,
            WorkShift.work_shift_from,
            WorkShift.work_shift_to,
        )
        .filter(WorkShift.vehicle_id == id)
        .all()
    )
    query_div = jsonable_encoder(query_div)
    query_work_shift = jsonable_encoder(query_work_shift)
    data = {"zone": query_div, "workShift": query_work_shift}
    return resp.success(data=data)
