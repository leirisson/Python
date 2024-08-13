from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base




class Settings(BaseSettings):
    """"    CONFIGURAÇÕES GERAIS DA APLICAÇÃO """
    
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:123456@localhost:5432/faculdade"
    DB_base_model: ClassVar = declarative_base()

    class Config:
        case_sensitive = True



settings = Settings()
