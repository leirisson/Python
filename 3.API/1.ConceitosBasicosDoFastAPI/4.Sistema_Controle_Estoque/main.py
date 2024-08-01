from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models.modelProduto import Produto

app  = FastAPI()


produtos_do_estoque = {
    1: {
        "nome": "caneta",
        "preco": 2.50,
        "quantidade": 100,
        "descricao": "caneta bic azul"
    },
    2: {
        "nome": "caderno",
        "preco": 15.00,
        "quantidade": 50,
        "descricao": "caderno espiral de 100 folhas"
    },
    3: {
        "nome": "lápis",
        "preco": 1.00,
        "quantidade": 200,
        "descricao": "lápis preto HB"
    },
    4: {
        "nome": "borracha",
        "preco": 0.75,
        "quantidade": 150,
        "descricao": "borracha branca"
    },
    5: {
        "nome": "apontador",
        "preco": 3.00,
        "quantidade": 80,
        "descricao": "apontador metálico com depósito"
    },
    6: {
        "nome": "marcador",
        "preco": 4.00,
        "quantidade": 60,
        "descricao": "marcador fluorescente verde"
    },
    7: {
        "nome": "clipe",
        "preco": 0.50,
        "quantidade": 300,
        "descricao": "clipe metálico para papel"
    },
    8: {
        "nome": "pastas",
        "preco": 6.00,
        "quantidade": 40,
        "descricao": "pastas plásticas com elástico"
    },
    9: {
        "nome": "tesoura",
        "preco": 5.00,
        "quantidade": 30,
        "descricao": "tesoura grande com cabo ergonômico"
    },
    10: {
        "nome": "glue",
        "preco": 2.75,
        "quantidade": 70,
        "descricao": "cola branca escolar"
    },
    11: {
        "nome": "canetinha",
        "preco": 3.50,
        "quantidade": 90,
        "descricao": "canetinha hidrográfica de 12 cores"
    },
    12: {
        "nome": " régua",
        "preco": 1.25,
        "quantidade": 120,
        "descricao": "régua transparente de 30 cm"
    },
    13: {
        "nome": "compasso",
        "preco": 4.50,
        "quantidade": 25,
        "descricao": "compasso de metal com ajustes"
    }
}


@app.get("/")
async def index():
    return {"msg": "home page da api"}


# listagem de todos os produtos disponíveis no estoque.
@app.get("/estoque")
async def get_estoque():
    return produtos_do_estoque


# Implementar a adição de novos produtos ao estoque, incluindo nome, descrição, preço e quantidade em estoque.
@app.post("/estoque")
async def criar_produto(produto: Produto):
    proximo_id = len(produtos_do_estoque) + 1
    produto.id = proximo_id
    try:
        if produto.id not in produtos_do_estoque:
            produtos_do_estoque[produto.id] = produto
            del produto.id
            return "produto cadastrado com sucesso."
    except KeyError as e:
        raise f"Error ao tentar criar um produro {e}"
    

# Implementar a atualização das informações dos produtos, permitindo a alteração do preço e da quantidade em estoque.
@app.patch("/estoque/{id_produto}")
async def atualizar_produto(id_produto: int, produto: Produto):
    try:
        if id_produto in produtos_do_estoque:
            print(produtos_do_estoque[id_produto])
            produtos_do_estoque[id_produto]["preco"] = produto.preco
            produtos_do_estoque[id_produto]["quantidade"] = produto.quantidade
            produtos_do_estoque[id_produto]
            return f"Preco: {produtos_do_estoque[id_produto]["preco"]} e Quantidade: {produtos_do_estoque[id_produto]["quantidade"]} atualizadados com sucesso."
    except:
        raise "Produto não cadastrado no estoque."

#  Implementar a remoção de produtos do estoque
@app.delete("/estoque/{id_produto}")
async def deletar_produto(id_produto: int):
    try:
        del produtos_do_estoque[id_produto]
        return "produto deletado"
    except KeyError as e:
        raise f"Error ao tentar excluir => {e}"





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="172.0.0.1", port=8080, debug=True, reload=True)