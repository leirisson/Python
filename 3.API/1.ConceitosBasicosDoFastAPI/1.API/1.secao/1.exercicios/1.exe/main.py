from typing import List, Optional
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

# importando model
from models.modelTarefa import Tarefa

app = FastAPI()

lista_de_tarefas = {
    1: {
        "titulo": "comprar pão",
        "descricao": "comprar pão todo dia",
        "data_de_vencimento": "20/10/2024",
        "status": "pendente"
    },
    2: {
        "titulo": "estudar Python",
        "descricao": "completar o curso de Python na Udemy",
        "data_de_vencimento": "25/08/2024",
        "status": "em progresso"
    },
    3: {
        "titulo": "limpar a casa",
        "descricao": "fazer a limpeza geral da casa",
        "data_de_vencimento": "21/07/2024",
        "status": "pendente"
    },
    4: {
        "titulo": "ir ao dentista",
        "descricao": "consulta de rotina no dentista",
        "data_de_vencimento": "30/09/2024",
        "status": "pendente"
    },
    5: {
        "titulo": "fazer compras",
        "descricao": "comprar itens para o mês",
        "data_de_vencimento": "05/08/2024",
        "status": "pendente"
    },
    6: {
        "titulo": "escrever relatório",
        "descricao": "escrever o relatório mensal do trabalho",
        "data_de_vencimento": "31/07/2024",
        "status": "em progresso"
    },
    7: {
        "titulo": "ir à academia",
        "descricao": "treino de musculação",
        "data_de_vencimento": "27/07/2024",
        "status": "concluído"
    },
    8: {
        "titulo": "reunião de trabalho",
        "descricao": "reunião semanal com a equipe",
        "data_de_vencimento": "29/07/2024",
        "status": "pendente"
    },
    9: {
        "titulo": "ler livro",
        "descricao": "ler 50 páginas do livro",
        "data_de_vencimento": "15/08/2024",
        "status": "em progresso"
    },
    10: {
        "titulo": "pagar contas",
        "descricao": "pagar as contas do mês",
        "data_de_vencimento": "10/08/2024",
        "status": "pendente"
    }
}


@app.get("/")
async def index():
    return {"heelo":"pagina inicial da API"}

@app.get("/tarefas")
async def get_tarefas():
    return lista_de_tarefas

@app.get("/tarefas/{id_tarefa}")
async def get_tarefa(id_tarefa: int):
    try:
        tarefa_pesquisada = lista_de_tarefas[id_tarefa]
        return tarefa_pesquisada
    except KeyError:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="tarefa não encontrada.")
    
@app.post("/tarefas")
async def criar_uma_tarefa(tarefa: Tarefa):
    
    proximo_id = len(lista_de_tarefas) + 1
    tarefa.id = proximo_id


    if tarefa.id not in lista_de_tarefas:
        lista_de_tarefas[tarefa.id] = tarefa
        del tarefa.id
        return "tarefa criada com sucesso."
    
@app.put("/tarefas/{id_tarefa}")
async def atualizar_status_da_tarefa(id_tarefa: int, tarefa: Tarefa):
    if id_tarefa in lista_de_tarefas:
        lista_de_tarefas[id_tarefa]["status"] = tarefa.status
        del tarefa.id 
        return f"status atualizado com sucesso, status atual: {tarefa.status}"
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Tarefa não existe.")
@app.delete("/tarefas/{id_tarefa}")
async def deletar_uma_tarefa(id_tarefa: int):
    try:
        if id_tarefa in  lista_de_tarefas:
                if "concluído" in lista_de_tarefas[id_tarefa]["status"]:
                    del lista_de_tarefas[id_tarefa]
                    return "Tarefa com status concluida foi removida."
                else:
                    return "Esta tarefa ainda não foi concluida."
    except KeyError:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080, debug=True, reload=True)