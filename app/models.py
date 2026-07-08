from pydantic import BaseModel
from datetime import datetime


class TemperatureReading(BaseModel):
    sensor: str
    temperature: float
    battery_voltage: float
    wifi_rssi: int | None = None
    uptime: int
    firmware: str
    measured_at: datetime
