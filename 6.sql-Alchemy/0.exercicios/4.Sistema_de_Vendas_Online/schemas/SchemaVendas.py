from typing import Optional

from pydantic import BaseModel as SCBaseModel 

class Schemavendas(SCBaseModel):
    id: Optional[int]
    nome_cliente: str
    nome_produto: str
    quantidade_produto: int

    class Config:
        from_attributes = True