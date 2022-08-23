import json
from datetime import datetime

from fastapi.encoders import jsonable_encoder

from app.models.customer import Customer
from app.models.electric_vehicle import Vehicle
from app.models.sale_information import SaleInformation
from app.schemas.response import resp


def get_list_coordinate_from_geolocation_type(coordinates=None):
    if not coordinates:
        return []
    try:
        coordinates = json.loads(coordinates)
        if not isinstance(coordinates, dict):
            return []
        features = coordinates.get("features", [])
        if not features:
            return []

        feature = features[0]
        result = feature.get("geometry", {}).get("coordinates", [])
        if not result:
            return []
        return result[0]
    except Exception:
        return []


def get_sale_information(id: str, db):
    query = (
        db.query(
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
        )
        .join(Vehicle)
        .join(Customer)
        .filter(
            SaleInformation.id == Vehicle.sale_id,
            SaleInformation.customer_id == Customer.id,
            Vehicle.id == id,
        )
        .first()
    )

    query = jsonable_encoder(query)
    if query:
        end_date = query.get("end_date")
        if end_date is not None:
            now = datetime.now().date()
            query["remaining_day"] = (
                datetime.strptime(end_date, "%Y-%m-%d").date() - now
            ).days
        query["coordinates"] = get_list_coordinate_from_geolocation_type(
            query["coordinates"]
        )

    return resp.success(data=query)
