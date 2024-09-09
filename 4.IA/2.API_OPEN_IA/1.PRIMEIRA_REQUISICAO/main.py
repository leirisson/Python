# importando arquivos necessarios
from chaveAPI import CHAVE_API
import requests
import json

# link de requisição - do tipo GET PARA VISUALIZAR TODOS OS MODELOS DE IAS GENERATIVAS
# link = "https://api.openai.com/v1/models"

# criando um dicionario de haders
headers = {
    "Authorization": f"Bearer {CHAVE_API}",
    "Content-Type":"application/json",
}

# REQUISIÇÃO PARA OBTER OS MODELOS DE IA 
#requisicao = requests.get(link, headers=headers)
#print(requisicao)
#print(requisicao.text)

# ================================ criando um requisição POST
# criando um prompt
msg_prompt = input("Digite seu prompt: ")

# ID DO MODEL GENERATIVO
id_modelo = "gpt-4o-mini"

#link da requisição do tipo POST
link_da_requisicao = "https://api.openai.com/v1/chat/completions"

# Request body
body_mensagem = {
    "model":id_modelo,
    "messages":[
        {"role":"user",
         "content":msg_prompt}
    ]
}

# parsando a mensagem para json
body_mensagem = json.dumps(body_mensagem)


# realizando a requisição

requisicao = requests.post(link_da_requisicao, headers=headers, data=body_mensagem)
print(requisicao)
print(requisicao.text)