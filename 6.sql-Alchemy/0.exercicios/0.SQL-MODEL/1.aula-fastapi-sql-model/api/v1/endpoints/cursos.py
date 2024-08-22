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
    
