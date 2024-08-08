from fastapi import FastAPI
from modelVenda import Venda
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Defina as origens permitidas
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://http://127.0.0.1:5500",
    "http://127.0.0.1:5500"
]

# Adicione o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Define as origens permitidas
    allow_credentials=True,          # Permite o envio de credenciais (cookies, autenticação HTTP)
    allow_methods=["*"],             # Permite todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],             # Permite todos os cabeçalhos HTTP
)




vendas = {
    "1": {
        "nome_cliente":"Leirisson Souza",
        "nome_produto":"Caderno 30 matérias",
        "quantidade_produto": 45,
        "valor_total": 135.00
    },
    "2": {
        "nome_cliente":"Maria Silva",
        "nome_produto":"Caneta esferográfica azul",
        "quantidade_produto": 100,
        "valor_total": 50.00
    },
    "3": {
        "nome_cliente":"João Pereira",
        "nome_produto":"Agenda 2024",
        "quantidade_produto": 30,
        "valor_total": 300.00
    },
    "4": {
        "nome_cliente":"Ana Souza",
        "nome_produto":"Bloco de notas",
        "quantidade_produto": 60,
        "valor_total": 180.00
    },
    "5": {
        "nome_cliente":"Carlos Santos",
        "nome_produto":"Lápis preto",
        "quantidade_produto": 150,
        "valor_total": 75.00
    }
}


@app.get("/")
async def alo():
    return {"hello":"loise"}

@app.get("/vendas")
async def pegar_todas_vendas():
    return  vendas





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True, reload=True)