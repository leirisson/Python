from typing import Optional
from pydantic import BaseModel

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    senha: str