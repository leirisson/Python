from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar

# configurações gerais usadas na aplicação
class Configuracoes(BaseSettings):
    API_v1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:123456@localhost:5432/estacionamento"
    DB_BASEMODEL:  ClassVar = declarative_base()

    class Config:
        case_sensitive = True



settings = Configuracoes()