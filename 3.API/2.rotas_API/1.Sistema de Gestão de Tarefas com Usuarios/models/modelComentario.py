

from pydantic import validator # type: ignore
from models.modelBaseEntity import BaseEntity

class Comment(BaseEntity):
    text_comment : str
    id_author : str
    id_task : str
    
    
    @validator('text_comment')
    def validar_comentario(cls, value):
        if len(value) < 10:
            raise ValueError("o comentario dete ter no minimo 10 caracteres")