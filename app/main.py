from fastapi import FastAPI
from .routers import articles
from .config.cors import setup_cors
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings


app = FastAPI()

setup_cors(app)

@app.include_router(articles.router)

@app.get('/')
async def root():
    return {'message': 'Blog api app'}

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}

@app.get("/config-check")
def config_check():
    return {
        "env": settings.env,
        "debug": settings.debug,
        "origins": settings.allowed_origins
    }