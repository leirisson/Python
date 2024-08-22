from fastapi import APIRouter
from api.v1.endpoints import cadastros


api_router = APIRouter()
api_router.include_router(cadastros.router, prefix='/cadastros', tags=["cadastros"])


