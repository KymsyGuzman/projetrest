from pydantic import BaseSettings
from dotenv import load_dotenv
import os
load_dotenv(".env")

class Settings(BaseSettings):
    app_name: str = "My App"
    SQLALCHEMY_DATABASE_URI: str = os.getenv("SQLALCHEMY_DATABASE_URI")
    ADMIN_EMAIL: str = os.getenv("ADMIN_EMAIL")

    class Config:
        env_file = ".env"

settings = Settings()
