from fastapi.encoders import jsonable_encoder

from app.models.charger import Charger
from app.models.electric_vehicle import Vehicle
from app.schemas.response import resp


def get_charger(id: str, db):
    query = (
        db.query(
            Charger.model,
            Charger.serial_number,
            Charger.charger_pdi_status,
        )
        .join(Vehicle)
        .filter(Charger.id == Vehicle.id, Vehicle.id == id)
        .first()
    )
    query = jsonable_encoder(query)
    return resp.success(data=query)
