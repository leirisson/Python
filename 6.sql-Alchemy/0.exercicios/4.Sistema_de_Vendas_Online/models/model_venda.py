from configs.configs import settings
from sqlalchemy import Column, String, Float, Integer # type: ignore


class Model_venda(settings.DB_BASE_MODEL):
    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_cliente = Column(String(100))
    nome_produto = Column(String(100))
    quantidade_produto = Column(Integer)
    

    class Config:
        orm_mode = True