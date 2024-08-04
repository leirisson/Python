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

feedbacks_of_client = { 
    1: {
        "name_client": "Leirisson Souza",
        "name_product": "Computador A520",
        "comment": "O computador é muito bom, mas precisa melhorar a memória RAM."
    },
    2: {
        "name_client": "Maria Silva",
        "name_product": "Smartphone X200",
        "comment": "A câmera é excelente, mas a bateria dura pouco."
    },
    3: {
        "name_client": "João Pereira",
        "name_product": "Notebook B300",
        "comment": "Desempenho ótimo, mas o preço é um pouco alto."
    },
    4: {
        "name_client": "Ana Souza",
        "name_product": "Tablet T10",
        "comment": "Muito bom para leitura, mas a tela poderia ser maior."
    },
    5: {
        "name_client": "Carlos Santos",
        "name_product": "Fone de Ouvido H600",
        "comment": "Som de alta qualidade, mas desconfortável para uso prolongado."
    },
    6: {
        "name_client": "Fernanda Lima",
        "name_product": "Impressora P300",
        "comment": "Impressão rápida, mas consome muita tinta."
    }
}



from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from models.modelFeedbeck import Feedback

app = FastAPI()

@app.get("/")
async def index():
    return {"msg":"hello, wellcom the API from feedback of client."}

# Read: Listar todos os feedbacks recebidos.
@app.get("/feedbacks")
async def all_feedbacks():
    return feedbacks_of_client

# Create: Adicionar um novo feedback
@app.post("/feedbacks")
async def create_feedback(feedback: Feedback):
    id_feedback = len(feedbacks_of_client) + 1
    feedback.id = id_feedback
    
    if feedback.id not in feedbacks_of_client:
        feedbacks_of_client[feedback.id] = feedback
        del feedbacks_of_client[feedback.id].id
        return f"create feedback with ID: {id_feedback}"
    else:
        return f"not was possible create comment."
    
    
# Update: Atualizar o feedback (comentários)
@app.patch("/feedbacks/{id_feedback}")
async def update_feedback_comment_of_user(id_feedback: int, feedback: Feedback):
    try:
        if id_feedback in feedbacks_of_client:
           feedbacks_of_client[id_feedback].comment = feedback.comment
           return "comment update with sucess."
    except KeyError as e:
        return f"Error in the update of comment.{e}"
    

# Delete: Remover um feedback. 
@app.delete("/feedbacks/{id_feedback}")
async def delete_feedback_client(id_feedback: int):
    if id_feedback in feedbacks_of_client:
        del feedbacks_of_client[id_feedback]
        return "feedback delete with sucess."
    else:
        return f"feedback with ID: {id_feedback} not in feedbacks."

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080, debug=True, reload=True)