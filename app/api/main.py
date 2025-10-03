from fastapi import APIRouter

from app.api.routers import articles

api_router = APIRouter()
api_router.include_router(articles.router)