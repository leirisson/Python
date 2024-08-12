from pydantic_settings import BaseSettings 
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar
class Configuracoes(BaseSettings):
    """
    Configurações gerais usada na aplicação

    """

    API_V1_STR: str = "/api/v1"
    DB_URL: str = "mysql+pymysql://root:123456@localhost:3307/faculdade"
    BD_base_model: ClassVar = declarative_base()

    class Config:
        case_sensitive = True


settings = Configuracoes()

