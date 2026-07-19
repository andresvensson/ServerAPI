from pydantic import BaseModel
from datetime import datetime


class TemperatureReading(BaseModel):
    sensor: str
    sensor_type: str

    temperature: float
    humidity: float | None = None
    battery_voltage: float | None = None

    measured_at: datetime

    wifi_rssi: int | None = None
    uptime: int
    firmware: str

    boot_reason: str | None = None
