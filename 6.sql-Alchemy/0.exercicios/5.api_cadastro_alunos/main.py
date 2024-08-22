from fastapi import FastAPI

from configuracoes_projeto.configuracoes import settings
from api.v1.api import api_router

app = FastAPI(title="Cadastro do aluno")

app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", host=8080, debug=True, reload=True, log_level=True)