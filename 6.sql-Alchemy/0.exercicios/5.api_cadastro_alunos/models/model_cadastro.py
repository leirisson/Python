

from configuracoes_projeto.configuracoes import settings
from sqlalchemy import Column, Integer, String

class Cadastro(settings.DB_BASE_MODEL):
    __tablename__ = "cadastros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    idade = Column(Integer)
    turma = Column(String(50))
    