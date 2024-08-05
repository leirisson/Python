from fastapi import FastAPI # type: ignore

app = FastAPI()

from routers import router_usuario
from routers import router_comentarios
from routers import router_tarefa
from routers import router_projetos



app.include_router(router_usuario.router, tags=["usuarios"])


if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app, host="0.0.0.0", port=8080, debug=True, reload=True)