from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Configuracoes(BaseSettings):
    """
    Configurações gerais usada na aplicação

    """

    API_V1_STR = "/api/v1"
    DB_URL = "mysql+pymysql://root:123456@localhost:3307/faculdade"
    BD_base_model = declarative_base()

    class Copnfig:
        case_sensitive = True


settings = Configuracoes()

