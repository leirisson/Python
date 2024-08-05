from pydantic import BaseModel, validator # type: ignore
from typing import Optional


class BaseEntity(BaseModel):
    id : Optional[int] = None
    name : str
    
    @validator('name')
    def validar_nome(cls, value: str):
        
        # validando o tamanho da string
        name = len(value)
        if name == 0 :
            raise ValueError("o nome não pode estar vazio")
        elif name <3 :
            raise ValueError("O nome deve ter mais de 3 caracteres")
        
        return value