from typing import Optional
from pydantic import BaseModel


class Publicacao(BaseModel):
    id: Optional[int] = None
    titulo: str
    autor: str
    ano_publicacao : int
