from sqlalchemy import Column, String, DateTime, Date, Float, ForeignKey
from datetime import datetime
from app.common.database import DBBaseCustom
from app.models.charger import Charger


from app.models.electric_vehicle_model import VehicleModel
from app.models.sale_information import SaleInformation


class Vehicle(DBBaseCustom):
    __tablename__ = "electric_vehicle"
    id = Column(String(255), unique=True, index=True, primary_key=True)
    creation = Column(DateTime,
                      nullable=False,
                      default=datetime.utcnow(), )
    modified = Column(DateTime,
                      nullable=False,
                      default=datetime.utcnow(),
                      onupdate=datetime.utcnow(), )
    modified_by = Column(String(255))
    owner = Column(String(255))
    vehicle_number = Column(String(255))
    serial_number = Column(String(255))
    model_id = Column(String(255), ForeignKey(VehicleModel.id))
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
    sale_id = Column(String(255), ForeignKey(SaleInformation.id))
    charger_id = Column(String(255), ForeignKey(Charger.id))