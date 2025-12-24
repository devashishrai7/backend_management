from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).parent

class Settings(BaseSettings):
    JWT_SECRET_KEY: str
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    class Config:
        env_file = BASE_DIR / ".env"
        env_file_encoding = "utf-8"
    
settings = Settings()