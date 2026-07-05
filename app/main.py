from fastapi import FastAPI
from app.models import TemperatureReading
from app.database import insert_temperature

app = FastAPI(
    title="Pico Temperature API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "application": "Pico Temperature API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "pico-temperature-api",
        "version": "0.1.0",
    }


@app.post("/api/v1/temperature")
def receive_temperature(reading: TemperatureReading):
    insert_temperature(reading)
    return {
        "message": "Temperature received and stored",
        "reading": reading,
    }

