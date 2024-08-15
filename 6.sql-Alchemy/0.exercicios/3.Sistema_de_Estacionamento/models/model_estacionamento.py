from core_config.configuracoes import settings
from sqlalchemy import Column, String, Integer

class Model_estacionamento(settings.DB_BASEMODEL):
    __tablename__ = "estacionamentos"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    modelo_carro: str = Column(String(100))
    placa_carro: str = Column(String(10))
    