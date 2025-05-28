from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .settings import settings


def setup_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_orgins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=['*'] if settings.env == 'dev' else ['GET', 'POST'],
        allow_headers=['*'] if settings.env == 'dev' else ['Authorization', 'content-type'],
    )