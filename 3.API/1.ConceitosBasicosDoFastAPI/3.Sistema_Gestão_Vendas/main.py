# 6. Sistema de Gestão de Vendas
# Crie uma API para gerenciar vendas de uma loja, com as seguintes funcionalidades:

# Create: Registrar uma nova venda com nome do cliente,
#  produto vendido,
#  quantidade
#  valor total.

# Read: Listar todas as vendas realizadas.
# Update: Atualizar informações da venda (quantidade, valor total).
# Delete: Cancelar uma venda.



from fastapi import FastAPI # type: ignore
from fastapi import HTTPException
from fastapi import status


from models.modelVenda import Venda
app = FastAPI()


vendas = {
    1: {
        "nome_cliente":"Leirisson Souza",
        "nome_produto":"Caderno 30 matérias",
        "quantidade_produto": 45,
        "valor_total": 135.00
    },
    2: {
        "nome_cliente":"Maria Silva",
        "nome_produto":"Caneta esferográfica azul",
        "quantidade_produto": 100,
        "valor_total": 50.00
    },
    3: {
        "nome_cliente":"João Pereira",
        "nome_produto":"Agenda 2024",
        "quantidade_produto": 30,
        "valor_total": 300.00
    },
    4: {
        "nome_cliente":"Ana Souza",
        "nome_produto":"Bloco de notas",
        "quantidade_produto": 60,
        "valor_total": 180.00
    },
    5: {
        "nome_cliente":"Carlos Santos",
        "nome_produto":"Lápis preto",
        "quantidade_produto": 150,
        "valor_total": 75.00
    }
}



@app.get("/")
async def index():
    return { "msg":"Bem-Vindo a API de registro de vendas."}


# Read: Listar todas as vendas realizadas.
@app.get("/vendas")
async def todas_as_vendas():
    return vendas


# Create: Registrar uma nova venda com nome do cliente
@app.post("/vendas")
async def criar_venda(venda: Venda):
    proximo_id = len(vendas) + 1
    venda.id = proximo_id
    if venda.id not in vendas:
        vendas[venda.id] = venda
        del venda.id
        return f"Venda realizada, nome produto: {venda.nome_produto}."
    
# Update: Atualizar informações da venda (quantidade, valor total).
@app.patch("/vendas/{id_venda}")
async def atualizar_venda(id_venda: int, venda: Venda):
    try:
        if id_venda in vendas:
            vendas[id_venda].quantidade_produto = venda.quantidade_produto
            vendas[id_venda].valor_total = venda.valor_total
            return f"venda editada com sucesso ID venda: {id_venda}"
        else:
            return f"ID: {id_venda} não encontrado."
    except KeyError as e:
        return f"Erro ao tentar editar venda erro: => {e}"



# Delete: Cancelar uma venda.
@app.delete("/vendas/{id_venda}")
async def deletar_venda(id_venda: int):
    try:
        if id_venda in vendas:
            del vendas[id_venda]
            return "deletado com sucesso."
        else:
            return "ID: {id_venda} não encontrado"
    except KeyError as e:
        return f"Deu erro ao tentar deletar: {e}"
        
        
    


if __name__ == "__main__":
    import uvicorn  # type: ignore
    uvicorn.run(app, host="127.0.0.1", port=8080, debug=True, reload=True)