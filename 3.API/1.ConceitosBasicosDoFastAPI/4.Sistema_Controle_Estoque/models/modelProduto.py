from pydantic import BaseModel
from typing import Optional

class Produto(BaseModel):
    id : Optional[int] = None
    nome : str
    preco : float
    quantidade : int
    descricao : str
    