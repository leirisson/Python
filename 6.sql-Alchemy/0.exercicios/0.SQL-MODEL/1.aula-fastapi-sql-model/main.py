from fastapi import FastAPI
from core.configuracoes import settings
from api.v1.api import api_router


app = FastAPI(title="Curso de API com Fastapi e sqml Model")
app.include_router(api_router, prefix=settings.API_V1_STR)



if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=8000,  log_level="info")