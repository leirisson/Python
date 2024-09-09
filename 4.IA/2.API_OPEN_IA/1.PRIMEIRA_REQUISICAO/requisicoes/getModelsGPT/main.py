# importando arquivos necessarios
from chaveAPI import CHAVE_API
import requests


# link de requisição - do tipo GET PARA VISUALIZAR TODOS OS MODELOS DE IAS GENERATIVAS
link = "https://api.openai.com/v1/models"

# criando um dicionario de haders
headers = {
    "Authorization": f"Bearer {CHAVE_API}",
    "Content-Type":"application/json",
}

# REQUISIÇÃO PARA OBTER OS MODELOS DE IA 
requisicao = requests.get(link, headers=headers)
print(requisicao)
print(requisicao.text)

