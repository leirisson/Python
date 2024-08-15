from pydantic_settings import BaseSettings 
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar

class Settings(BaseSettings):
    # configurações gerais da APLICAÇÂO
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "mysql+aiomysql://root:123456@localhost:3307/vendas"
    DB_BASE_MODEL: ClassVar = declarative_base()


    class config:
        case_sensitive = True

settings = Settings()


