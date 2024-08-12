# 1. Sistema de Biblioteca
# Crie uma API para gerenciar uma biblioteca com livros, revistas e jornais.
# Implemente as operações de CRUD para cada tipo de publicação e 
# adicione endpoints para consultar, adicionar, atualizar e deletar publicações.

# Objetivos:
# Criar classes base Publicacao e classes derivadas Livro, Revista e Jornal.
# Implementar métodos para gerenciar publicações.
# Utilizar herança e polimorfismo para as operações comuns.
# Endpoints sugeridos:

# GET /publicacoes
# GET /publicacoes/{id}
# POST /publicacoes
# PUT /publicacoes/{id}
# DELETE /publicacoes/{id}

from models.model_Livro import Livro
from models.model_Jornal import Jornal
from models.model_Revista import Revista

from fastapi import FastAPI 

from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("postgresql://postgres:123456@localhost:5432/cadastro")
conexao  = engine.connect()
comando_sql = text("SELECT * FROM cadastros")

response = conexao.execute(comando_sql)

lista_cadastro = []

for cadstro in response:
    lista_cadastro.append(cadstro)

dados_biblioteca =[
    {'id': 1, 'titulo': 'Python para Todos', 'autor': 'Autor Desconhecido', 'ano_publicacao': 2023, 'numero_paginas': 350, 'editora': 'Editora ABC'},
    {'id': 2, 'titulo': 'Aprendendo SQL', 'autor': 'Outro Autor', 'ano_publicacao': 2022, 'numero_paginas': 250, 'editora': 'Editora XYZ'},
    {'id': 3, 'titulo': 'Revista de Tecnologia', 'autor': 'Jane Doe', 'ano_publicacao': 2023, 'volume': 15, 'numero': 4},
    {'id': 4, 'titulo': 'Revista de Ciência', 'autor': 'John Smith', 'ano_publicacao': 2022, 'volume': 30, 'numero': 12},
    {'id': 5, 'titulo': 'Fundamentos de Machine Learning', 'autor': 'Alice Johnson', 'ano_publicacao': 2021, 'numero_paginas': 400, 'editora': 'Editora Tech'},
    {'id': 6, 'titulo': 'Introdução à Ciência de Dados', 'autor': 'Robert Brown', 'ano_publicacao': 2020, 'numero_paginas': 320, 'editora': 'Editora Data'},
    {'id': 7, 'titulo': 'Revista de Programação', 'autor': 'Emily Davis', 'ano_publicacao': 2021, 'volume': 22, 'numero': 6},
    {'id': 8, 'titulo': 'Revista de Inteligência Artificial', 'autor': 'Michael Wilson', 'ano_publicacao': 2022, 'volume': 18, 'numero': 3},
    {'id': 9, 'titulo': 'História da Computação', 'autor': 'Sarah Lee', 'ano_publicacao': 2019},
    {'id': 10, 'titulo': 'Avanços em Tecnologia', 'autor': 'David Clark', 'ano_publicacao': 2020}
]




#criando app 
app = FastAPI()

@app.get("/")
async def index():
    return {"msg": "Home page da API de Biblioteca"}

@app.get("/publicacoes")
async def get_dados_biblioteca():
    return lista_cadastro

if __name__ == "__main__":
    import uvicorn 

    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True, reload=True)