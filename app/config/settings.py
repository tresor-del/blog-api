from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    env: str
    debug: bool
    allowed_origins: List[str]  

    class Config:
        env_file = os.getenv('ENV_FILE', '.env.dev')

settings = Settings()