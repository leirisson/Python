####################################################
# 7. Sistema de Feedback de Clientes               #
# Crie uma API para gerenciar feedbacks de clientes#
# com as seguintes funcionalidades:                #
####################################################
# Create: Adicionar um novo feedback com:          #
# 1 - nome do cliente,                             #
# 2 - produto,                                     #
# 3 - comentários.                                 #
# Read: Listar todos os feedbacks recebidos.       #
# Update: Atualizar o feedback (comentários).      #
# Delete: Remover um feedback.                     #
####################################################

from pydantic import BaseModel
from typing import Optional

class Feedback(BaseModel):
    id : Optional[int] = None
    name_client : str
    name_product : str
    comment : str
    