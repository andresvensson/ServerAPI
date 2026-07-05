from pydantic import BaseModel


class TemperatureReading(BaseModel):
    sensor: str
    temperature: float
    battery_voltage: float