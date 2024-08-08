from pydantic import BaseModel
from typing import Optional



# 6. Sistema de Gestão de Vendas
# Crie uma API para gerenciar vendas de uma loja, com as seguintes funcionalidades:

# Create: Registrar uma nova venda com nome do cliente,
#  produto vendido,
#  quantidade
#  valor total.

# Read: Listar todas as vendas realizadas.
# Update: Atualizar informações da venda (quantidade, valor total).
# Delete: Cancelar uma venda.



class Venda(BaseModel):
    id : Optional[int] = None
    nome_cliente : str
    nome_produto : str
    quantidade_produto : int
    valor_total : float