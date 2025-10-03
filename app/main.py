from fastapi import FastAPI

from app.config.cors import setup_cors
from app.config.settings import settings
from app.api.main import api_router


app = FastAPI()

setup_cors(app)

app.include_router(api_router)

@app.get('/')
async def root():
    return {'message': 'Blog api app'}

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}

@app.get("/config-check")
def config_check():
    return {
        "DEBUG": settings.DEBUG,
        "ORIGINS": settings.ALLOWED_ORIGINS
    }