from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from models.modelConsulta import Consulta

app  = FastAPI()

@app.get("/")
async def index():
    return { "msg" : "boas vindas a API de consulta"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080, debug=True, reload=True)

    