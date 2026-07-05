from fastapi import FastAPI


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


