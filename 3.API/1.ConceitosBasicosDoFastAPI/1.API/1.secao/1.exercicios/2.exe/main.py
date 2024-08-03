from fastapi import FastAPI
from typing import Optional
from fastapi import HTTPException
from fastapi import status


#importando o model de Usuario
from models.modelUsuario import Usuario


#lista de usuarios cadastrados
lista_de_usuarios = {
    1: {
        "nome": "Leirisson Souza",
        "email": "leirisson@email.com",
        "senha": "leirisson@123"
    },
    2: {
        "nome": "Ana Silva",
        "email": "ana.silva@email.com",
        "senha": "ana@456"
    },
    3: {
        "nome": "Carlos Pereira",
        "email": "carlos.pereira@email.com",
        "senha": "carlos@789"
    },
    4: {
        "nome": "Beatriz Oliveira",
        "email": "beatriz.oliveira@email.com",
        "senha": "beatriz@321"
    },
    5: {
        "nome": "Daniel Costa",
        "email": "daniel.costa@email.com",
        "senha": "daniel@654"
    },
    6: {
        "nome": "Eduarda Santos",
        "email": "eduarda.santos@email.com",
        "senha": "eduarda@987"
    },
    7: {
        "nome": "Felipe Lima",
        "email": "felipe.lima@email.com",
        "senha": "felipe@123"
    },
    8: {
        "nome": "Gabriela Mendes",
        "email": "gabriela.mendes@email.com",
        "senha": "gabriela@456"
    },
    9: {
        "nome": "Henrique Alves",
        "email": "henrique.alves@email.com",
        "senha": "henrique@789"
    },
    10: {
        "nome": "Isabela Ferreira",
        "email": "isabela.ferreira@email.com",
        "senha": "isabela@321"
    }
}



# criando app
app = FastAPI()

@app.get("/")
async def index():
    return {"mensagem inicial":"bem-vindo a API de Gestão de Usuários"}


#buscar todos os usuarios
@app.get("/usuarios")
async def lista_usuarios():
    return lista_de_usuarios


# buscar um usuario por ID
@app.get("/usuarios/{id_usuario}")
async def lista_usuario(id_usuario: int):
    try:
        usuario_encontrado = lista_de_usuarios[id_usuario]
        return usuario_encontrado
    except KeyError:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Usuario com o ID: {id_usuario}, não esta cadastrado.")

# criar um usuario
@app.post("/usuarios")
async def criar_usuario(usuario: Usuario):
    try:
        proximo_id = len(lista_de_usuarios) + 1
        usuario.id = proximo_id

        if usuario.id not in lista_de_usuarios:
            lista_de_usuarios[usuario.id] = usuario
            del usuario.id
            return "usuario criado com sucesso"
        
    except KeyError:
        return f"Erro ao tentar criar um usuario: {KeyError}"
    
# atualizar informações do cliente
@app.patch("/usuarios/{id_usuario}")
async def editar_dados_usuario(id_usuario: int, usuario: Usuario):
    try:
        if id_usuario in lista_de_usuarios:
            lista_de_usuarios[id_usuario]['nome'] = usuario.nome
            lista_de_usuarios[id_usuario]['email'] = usuario.email
            del usuario.id
            return "Dados atualizado com sucesso."
    except KeyError:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado.")


# deletando um usuario 
@app.delete("/usuarios/{id_usuario}")
async def deletar_usuario(id_usuario: int):
    try:
        if id_usuario in lista_de_usuarios:
            del lista_de_usuarios[id_usuario]
            return "Usuario deletado com sucesso."
    except KeyError:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Usuario sem registros.")
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port='8080', debug=True, reload=True)
