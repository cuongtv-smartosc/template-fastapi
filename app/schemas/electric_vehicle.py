from pydantic import BaseModel


class VehicleBase(BaseModel):
    id: str = None


class VehicleResponse(VehicleBase):
    """This the serializer exposed on the API"""
    vehicle_number: str = None
    model_id: str = None
    sale_type: str = None
    edge_id: str = None
    customer_name: str = None
    operation_status: str = None


class VehicleCreate(VehicleBase):
    """This is the serializer used for POST/PATCH requests"""
    creation: str = None
    modified: str = None
    modified_by: str = None
    owner: str = None
    vehicle_number: str = None
    customer_name: str = None
    sale_id: str = None
    serial_number: str = None
    model_id: str = None
    car_condition: str = None
    forklift_pdi_status: str = None
    charger_id: str = None
