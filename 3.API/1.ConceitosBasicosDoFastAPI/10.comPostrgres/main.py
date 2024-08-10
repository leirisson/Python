from fastapi import FastAPI

app = FastAPI()


from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("postgresql://postgres:123456@localhost:5432/cadastro")
conexao  = engine.connect()
comando_sql = text("SELECT * FROM cadastros")

response = conexao.execute(comando_sql)

lista_cadastro = []

for cadastro in response:
    lista_cadastro.append(cadastro)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/cadastros")
async def load():
    return lista_cadastro


if __name__ == "__main__":
    import uvicorn  # type: ignore
    uvicorn.run(app, host="127.0.0.1", port=8080, debug=True, reload=True)