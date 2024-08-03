
from pydantic import BaseModel
from typing import Optional

class Tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    data_de_vencimento: str
    status: str

