from fastapi import APIRouter
from api.V1.endpoints import vendas

api_router = APIRouter()
api_router.include_router(vendas.router, prefix='/vendas', tags=["vendas"])


