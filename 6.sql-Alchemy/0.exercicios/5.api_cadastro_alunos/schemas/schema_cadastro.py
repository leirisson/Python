from typing import Optional
from pydantic import BaseModel as SC_Base_model

class Schemacadastro(SC_Base_model):
    id: Optional[int]
    nome: str
    idade: int
    turma: str

    class Config:
        orm_mode = True
        