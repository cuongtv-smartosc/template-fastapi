from sqlalchemy import Column, String, DateTime, Date, Float, ForeignKey
from datetime import datetime

from sqlalchemy.orm import relationship

from app.common.database import DBBaseCustom
from app.models.charger import Charger
from app.models.electric_vehicle_customer import VehicleCustomer
from app.models.electric_vehicle_sale_information import VehicleSaleInformation


class Vehicle(DBBaseCustom):
    __tablename__ = "tabElectric Vehicle"
    id = Column(String(255), unique=True, index=True, primary_key=True)
    creation = Column(DateTime,
                      nullable=False,
                      default=datetime.utcnow(), )
    # description = Column(String(255))
    modified = Column(DateTime,
                      nullable=False,
                      default=datetime.utcnow(),
                      onupdate=datetime.utcnow(), )
    modified_by = Column(String(255))
    owner = Column(String(255))
    vehicle_number = Column(String(255))
    serial_number = Column(String(255))
    model_id = Column(String(255))
    car_condition = Column(String(255))
    forklift_pdi_status = Column(String(255))

    import_date = Column(Date)
    manufactoring_date = Column(Date)
    asset_register_date = Column(Date)
    delivering_date = Column(Date)
    edge_id = Column(String(255))
    operating_hours = Column(String(255))
    operating_mileage = Column(String(255))
    initial_operating_hours = Column(Float, default=0.000000000)
    initial_operating_mileage = Column(Float, default=0.000000000)
    operation_status = Column(String(255))
    mileage_value = Column(String(255))
    hr = Column(String(255))
    customer_id = Column(String(255), ForeignKey(VehicleCustomer.id))
    sale_id = Column(String(255), ForeignKey(VehicleSaleInformation.id))
    charger_id = Column(String(255), ForeignKey(Charger.id))

