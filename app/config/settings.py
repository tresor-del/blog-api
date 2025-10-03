from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
import os

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file= ".env.dev"
    )

    DEBUG: bool = True
    ALLOWED_ORIGINS: List[str] = ["*"]
    DATABASE_URL: str = "sqlite:///./test.db"


settings = Settings()