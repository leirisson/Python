from typing import List


from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.curso_model import Curso_model
from core.dependencias import get_session

# BYPASS WARNING SQLMODEL SELECT 
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True
# FIM DO BYPASS 


router = APIRouter()

# POST Curso
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Curso_model)
async def criar_curso(curso: Curso_model, db: AsyncSession = Depends(get_session)):
    novo_curso = Curso_model(titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)

    db.add(novo_curso)
    await db.commit()


    return novo_curso

#get cursos 
@router.get("/", response_model=List[Curso_model])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Curso_model)
        resultado = await session.execute(query)
        cursos: List[Curso_model] = resultado.scalars().all()

        return cursos
    
# pegar um curso por id 
@router.get("/{id_curso}", response_model=Curso_model, status_code=status.HTTP_200_OK)
async def pegar_um_curso(id_curso: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Curso_model).filter(Curso_model.id == id_curso)
        result = await session.execute(query)
        curso: Curso_model = result.scalar_one_or_none()
        if curso:
            return curso
        else:
            raise HTTPException(detail="Curso não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        
# put => atualizar curso 
@router.put("/{id_curso}", status_code=status.HTTP_202_ACCEPTED, response_model=Curso_model)
async def atualizar_curso(id_curso: int, curso: Curso_model, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Curso_model).filter(Curso_model.id == id_curso)
        result = await session.execute(query)
        curso_update: Curso_model = result.scalar_one_or_none()
        if curso_update:
            curso_update.titulo = curso.titulo
            curso_update.aulas = curso.aulas
            curso_update.horas = curso.horas

            await session.commit()

            return curso_update
        else:
            raise HTTPException(detail="Curso não encontrado", status_code=status.HTTP_404_NOT_FOUND)

#deletar um curso
@router.delete("/{id_curso}", status_code=status.HTTP_204_NO_CONTENT)
async def deletando_um_curso(id_curso: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Curso_model).filter(Curso_model.id == id_curso)
        result = await session.execute(query)
        curso_delete = Curso_model = result.scalar_one_or_none()

        if curso_delete:
            await session.delete(curso_delete)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Curso não encontrado", status_code=status.HTTP_404_NOT_FOUND)