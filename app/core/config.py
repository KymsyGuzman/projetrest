from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "My App"
    admin_email: str
    items_per_page: int = 10

    class Config:
        env_file = ".env"

settings = Settings()