from pydantic_settings import BaseSettings 
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar
class Configuracoes(BaseSettings):
    """
    Configurações gerais usada na aplicação

    """

    API_V1_STR: str = "/api/v1"
    DB_URL: str = "mysql+aiomysql://root:123456@localhost:3307/faculdade"
    BD_base_model: ClassVar = declarative_base()
    DB_HOST: str = 'localhost'
    DB_PORT: int = 3307

    class Config:
        case_sensitive = True


settings = Configuracoes()

