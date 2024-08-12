from core_config.base import Base
from sqlalchemy import Column, String


# Endidade cadastros
class Cadastros(Base):
    __tablename__ = "cadastros"

    nome = Column(String, primary_key=True)
    email = Column(String, nullable=False)
    senha = Column(String, nullable=False)

    def __repr__(self):
        return f"Cadastro: nome={self.nome}, email={self.email}, senha={self.senha}"
    