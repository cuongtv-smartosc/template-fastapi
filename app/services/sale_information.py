import json
from datetime import datetime

from fastapi.encoders import jsonable_encoder

from app.common.handle_error import NotFoundException
from app.common.util import check_role_supervisor, get_company_id_from_user
from app.models.customer import Customer
from app.models.electric_vehicle import Vehicle
from app.models.sale_information import SaleInformation


def get_list_coordinate_from_geolocation_type(coordinates=None):
    if not coordinates:
        return []
    try:
        coordinates = json.loads(coordinates)
        return coordinates
    except:
        return []


def get_by_id(id, db, current_user):
    query = db.query(
        SaleInformation.sale_type,
        SaleInformation.sale_order_number,
        Customer.customer_name,
        Customer.address,
        SaleInformation.location,
        Vehicle.delivering_date,
        SaleInformation.vehicle_warranty,
        SaleInformation.battery_warranty,
        SaleInformation.battery_maintenance,
        SaleInformation.service,
        SaleInformation.start_date,
        SaleInformation.end_date,
        SaleInformation.coordinates,
        SaleInformation.contract_no,
    ).filter(
        SaleInformation.id == Vehicle.sale_id,
        SaleInformation.customer_id == Customer.id,
        Vehicle.id == id,
    )
    if not check_role_supervisor(current_user):
        company = get_company_id_from_user(current_user, db)
        query = query.filter(
            Customer.company_id.in_(company),
        )
    return query.first()


def get_sale_information(id, db, current_user):
    sale_info = jsonable_encoder(get_by_id(id, db, current_user))
    if not sale_info:
        raise NotFoundException(f"{id} is not existed")
    end_date = sale_info.get("end_date")
    if end_date is not None:
        now = datetime.now().date()
        sale_info["remaining_day"] = (
            datetime.strptime(end_date, "%Y-%m-%d").date() - now
        ).days
    sale_info["coordinates"] = get_list_coordinate_from_geolocation_type(
        sale_info["coordinates"]
    )
    return sale_info
