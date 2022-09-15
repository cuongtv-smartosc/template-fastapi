from datetime import datetime

from fastapi.encoders import jsonable_encoder

from app.common.handle_error import NotFoundException
from app.common.util import check_role_supervisor, get_company_id_from_user
from app.common.util import json_load as json_load
from app.models.customer import Customer
from app.models.electric_vehicle import Vehicle
from app.models.sale_information import SaleInformation


def get_list_coordinate(coordinates=None):
    if not coordinates:
        return []
    try:
        return json_load(coordinates)
    except Exception:
        return []


def get_by_id(id, db, current_user):
    query = db.query(
        SaleInformation.id,
        SaleInformation.sale_type,
        SaleInformation.sale_order_number,
        SaleInformation.customer_id,
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
    sale_information = jsonable_encoder(get_by_id(id, db, current_user))
    if not sale_information:
        raise NotFoundException(f"{id} is not existed")
    end_date = sale_information.get("end_date")
    sale_information["remaining_day"] = None
    if end_date is not None:
        now = datetime.now().date()
        sale_information["remaining_day"] = (
            datetime.strptime(end_date, "%Y-%m-%d").date() - now
        ).days
    sale_information["coordinates"] = get_list_coordinate(
        sale_information["coordinates"]
    )
    return sale_information
