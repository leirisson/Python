from typing import Optional
from pydantic import BaseModel

class Consulta(BaseModel):
    id : Optional[int] = None
    nome_cliente : str
    nome_medico : str
    data_consulta : str
    hora_consulta : str
    