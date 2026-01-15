from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_NAME: str = "Simple POS"
    DATABASE_URL: str = "sqlite:///./pos.db"

settings = Settings()
