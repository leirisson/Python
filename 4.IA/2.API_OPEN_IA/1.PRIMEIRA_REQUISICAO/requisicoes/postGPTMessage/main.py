# importando arquivos necessarios
from chaveAPI import CHAVE_API
import requests
import json
import os

# ID DO MODEL GENERATIVO
id_modelo = "gpt-4o-mini"

# criando um dicionario de haders
headers = {
    "Authorization": f"Bearer {CHAVE_API}",
    "Content-Type":"application/json",
}

# criando um prompt
os.system('cls')
titulo = "CONEXÃO COM A API DA openIA"
print(len(titulo) * "#")
print(titulo)
print(len(titulo) * "#")

msg_prompt = input("Digite seu prompt: ")

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
resposta = requisicao.json()

mensagem = resposta["choices"][0]["message"]["content"]

# exibindo resultado
os.system('cls')
print(len(titulo) * "#")
print(titulo)
print(len(titulo) * "#")
print(mensagem)
