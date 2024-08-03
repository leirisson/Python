from typing import List, Optional

from fastapi import FastAPI 
from fastapi import HTTPException
from fastapi import status

from models.modelCurso import Curso

cursos = {
    1: {
        "titulo" : "Programação c++",
        "aulas": 112,
        "horas": 80
    },
     2: {
        "titulo" : "Programação em python",
        "aulas": 160,
        "horas": 100
    },
     3: {
        "titulo" : "Programação JAVA",
        "aulas": 200,
        "horas": 150
    },

}

app = FastAPI()

@app.get("/")
async def index():
    return {"msg": "Pagina inicial da aplixação"}


@app.get("/cursos")
async def home():
    return cursos



@app.get("/cursos/{id_curso}")
async def get_curso(id_curso: int):
    try:
        curso_pesquisado = cursos[id_curso]
        return curso_pesquisado
    except KeyError:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Curso não encontrado")

    
@app.post("/cursos")
async def criar_curso(curso: Curso, status_code=status.HTTP_201_CREATED):
    id = len(cursos) + 1
    curso.id = id
    if curso.id not in  cursos:
        cursos[curso.id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, 
                            detail= f"ja existe um curso com o ID: {curso.id}")


@app.put("/cursos/{id_curso}")
async def atualizar_curso(id_curso: int, curso: Curso):
    if id_curso in cursos:
        cursos[id_curso] = curso
        del curso.id # deletando o id do curso, ainda não estamos usando
        return curso
    else:
        raise HTTPException(status = status.HTTP_404_NOT_FOUND, 
                            detail=f"Não existe um curso com o ID: {id_curso}")

@app.delete("/cursos/{id_curso}")
async def deletar_curso(id_curso:int):
    try:
        if id_curso in cursos:
            del cursos[id_curso]
            return "Curso deletado com sucesso."
    except KeyError:
        raise  HTTPException(statsu = status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="172.0.0.1", port=8000, debug=True, reload=True)