#    Usuários:
#    Create: Adicionar um novo usuário com nome, email e senha.
#    Read: Listar todos os usuários cadastrados.
#    Update: Atualizar informações do usuário (nome, email).
#    Delete: Remover um usuário do sistema.

from fastapi import APIRouter # type: ignore
from fastapi import HTTPException # type: ignore
from fastapi import status # type: ignore

from models.modelUsuario import User

router = APIRouter()


list_users = {
    
    1: {
        "name": "Leirisson Souza dos Santos",
        "email": "leirisson@email.com.br",
        "password": "123@souza"
    },
    2: {
        "name": "Maria Silva",
        "email": "maria.silva@example.com",
        "password": "maria123"
    },
    3: {
        "name": "João Pereira",
        "email": "joao.pereira@example.com",
        "password": "joao123"
    },
    4: {
        "name": "Ana Souza",
        "email": "ana.souza@example.com",
        "password": "ana123"
    },
    5: {
        "name": "Carlos Santos",
        "email": "carlos.santos@example.com",
        "password": "carlos123"
    },
    6: {
        "name": "Fernanda Lima",
        "email": "fernanda.lima@example.com",
        "password": "fernanda123"
    },
    7: {
        "name": "Ricardo Alves",
        "email": "ricardo.alves@example.com",
        "password": "ricardo123"
    }
}

#Read: Listar todos os usuários cadastrados.
@router.get("/api/v1/usuarios")
async def get_all_usuarios():
    return list_users

#Read: Listar apenas um usuários cadastrados.
@router.get("/api/v1/usuarios/{id_usuario}") 
async def get_one_user(id_usuario: int):
    try:
        user = list_users[id_usuario]
        return user
    except KeyError:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado")

@router.post("/api/v1/usuarios")
async def create_user(usuario: User):
    next_id = len(list_users) + 1
    usuario.id = next_id
    
    try:
        list_users[usuario.id] = usuario
        del usuario.id
        return "usuario criado com sucesso"
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não foi possivel criar um usuario")


#    Update: Atualizar informações do usuário (nome, email).
@router.patch("/api/v1/usuarios/{id_usuario}")
async def update_user(id_usuario: int , usuario: User):
    try:
        list_users[id_usuario].name = usuario.name
        list_users[id_usuario].email = usuario.email
        return "name and email update sucess."
    except KeyError:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="id not found")
    
        
#    Delete: Remover um usuário do sistema.
@router.delete("/api/v1/usuarios/{id_usuario}")
async def delete_user(id_usuario: int):
    try: 
        del list_users[id_usuario]
        return "congratulation, you deleted user whith sucess"
    except KeyError:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="user not int data base.")