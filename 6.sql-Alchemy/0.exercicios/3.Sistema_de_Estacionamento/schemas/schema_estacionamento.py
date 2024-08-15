from typing import Optional
from pydantic import BaseModel as SCBaseModel


class Schema_estacionamento(SCBaseModel):
    id: Optional[int]
    modelo_carro: str
    placa_carro: str

    class Config:
        orm_mode = True