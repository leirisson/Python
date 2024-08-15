from typing import List


from fastapi import APIRouter
from fastapi import status
from fastapi import HTTPException
from fastapi import Response
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.model_venda import Model_venda
from schemas.SchemaVendas import Schemavendas
from configs.dependences import get_session

router = APIRouter()

# criando um curso 
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Schemavendas)
async def criar_venda(venda: Schemavendas, db: AsyncSession = Depends(get_session)):
    nova_venda = Model_venda(nome_cliente=venda.nome_cliente,
                            nome_produto=venda.nome_produto, 
                            quantidade_produto = venda.quantidade_produto)
    
    db.add(nova_venda)
    await db.commit()

    return nova_venda
    
# get Cursos 
@router.get('/', response_model=List[Schemavendas])
async def pegar_todos_os_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Model_venda)
        resultado = await session.execute(query)
        venda: List[Model_venda] = resultado.scalars().all()
        return venda
    
# get gurso
@router.get('/{id_venda}', response_model=Schemavendas, status_code=status.HTTP_200_OK)
async def get_venda(id_venda: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Model_venda).filter(Model_venda.id == id_venda)
        resultado = await session.execute(query)
        venda  = resultado.scalar_one_or_none()

        if venda: 
            return venda
        else:
            raise HTTPException(detail='venda não encontrada.', status_code=status.HTTP_404_NOT_FOUND)
        
#put curso
@router.put("/{id_venda}", response_model=Schemavendas, status_code=status.HTTP_202_ACCEPTED)
async def put_venda(id_venda: int, venda: Schemavendas, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Model_venda).filter(Model_venda.id == id_venda)
        resultado = await session.execute(query)
        venda_update = resultado.scalar_one_or_none()

        if venda_update:
            
            venda_update.nome_cliente = venda.nome_cliente
            venda_update.nome_prosuto = venda.nome_produto
            venda_update.quantidade_produto = venda.quantidade_produto

            await session.commit()
            return venda_update
        else:
            raise HTTPException(detail='Venda não encontrado.', status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete("/{id_venda}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_venda(id_venda: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Model_venda).filter(Model_venda.id == id_venda)
        resultado = await session.execute(query)
        venda_del = resultado.scalar_one_or_none()

        if id_venda:
            await session.deletar(id_venda)
            session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Venda não ecnconto", status_code=status.HTTP_404_NOT_FOUND)
