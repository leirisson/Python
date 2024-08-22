from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.model_cadastro import Cadastro
from schemas.schema_cadastro import Schema_cadastro
from configuracoes_projeto.config_dependencias import get_session


router = APIRouter

# criando cadastro
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Schema_cadastro)
async def criar_um_cadastro(cadastro: Schema_cadastro, db: AsyncSession = Depends(get_session)):
    novo_cadastro  = Cadastro(nome=cadastro.nome,
                              idade=cadastro.idade,
                              turma=cadastro.turma
                              )
    db.add(novo_cadastro)
    await db.commit()
    return novo_cadastro


@router.get("/", response_model=List[Schema_cadastro])
async def pegar_todos_os_cadastros(db: AsyncSession = Depends(get_session)):
    async with db  as session:
        query = select(Cadastro)
        result = await session.execute(query)
        cadastros: List[Cadastro] = result.scalars().all()

        return  cadastros
