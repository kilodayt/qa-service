from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "QA Service"
    API_V1_STR: str = "/"
    DATABASE_URL: str
    DB_ECHO: bool = Field(default=False)

    # pydantic v2 стиль конфигурации
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
