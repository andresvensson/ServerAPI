from pydantic import BaseModel
from datetime import datetime


class TemperatureReading(BaseModel):
    sensor: str
    temperature: float
    battery_voltage: float
    measured_at: datetime
