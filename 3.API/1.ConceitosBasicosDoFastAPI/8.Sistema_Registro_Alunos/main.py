# ####################################################################
# 9. Sistema de Registro de Alunos                                   #
# Crie uma API para gerenciar o registro de alunos em uma escola,    #
# com as seguintes funcionalidades:                                  #
# ####################################################################
# Create: Registrar um novo aluno com:                               #
# 1 - nome                                                           #
# 2 - idade                                                          #
# 3 - série                                                          #
# 4 - turma.                                                         #
# Read: Listar todos os alunos registrados.                          #
# Update: Atualizar informações do aluno (série, turma).             #
# Delete: Remover um aluno do registro.                              #
# ####################################################################

from fastapi import FastAPI # type: ignore

from models.modelAluno import Aluno

list_registry_all_students = {
    1: {
        "name_student": "Leirisson Souza",
        "age": 25,
        "school_grade": "9º ano",
        "school_class": "morning"
    },
    2: {
        "name_student": "Maria Silva",
        "age": 14,
        "school_grade": "8º ano",
        "school_class": "afternoon"
    },
    3: {
        "name_student": "João Pereira",
        "age": 15,
        "school_grade": "9º ano",
        "school_class": "morning"
    },
    4: {
        "name_student": "Ana Souza",
        "age": 13,
        "school_grade": "7º ano",
        "school_class": "afternoon"
    },
    5: {
        "name_student": "Carlos Santos",
        "age": 16,
        "school_grade": "1º ano do Ensino Médio",
        "school_class": "morning"
    },
    6: {
        "name_student": "Fernanda Lima",
        "age": 17,
        "school_grade": "2º ano do Ensino Médio",
        "school_class": "afternoon"
    },
    7: {
        "name_student": "Ricardo Alves",
        "age": 18,
        "school_grade": "3º ano do Ensino Médio",
        "school_class": "morning"
    }
}


app = FastAPI()


@app.get("/")
async def index():
    return {"msg": " welcom to API "}

# Read: Listar todos os alunos registrados
@app.get("/students")
async def all_students_registry():
    return list_registry_all_students

# Create: Registrar um novo aluno
@app.post("/students")
async def create_new_studend(student: Aluno):
    next_id = len(list_registry_all_students) + 1
    student.id = next_id
    
    if student.id not in list_registry_all_students:
        list_registry_all_students[student.id] = student
        del student.id
        return f"Student create with sucess ID: {next_id}"
    else:
        return "Not possible create new student"


# Update: Atualizar informações do aluno (série, turma).           
@app.patch("/students/{id_student}")
async def update_student(id_student: int, student: Aluno):
    
    if id_student in list_registry_all_students:
        list_registry_all_students[id_student].school_grade = student.school_grade
        list_registry_all_students[id_student].school_class = student.school_class
        return "data update with sucess."
    else:
        return "not possible update the data of student"


# Delete: Remover um aluno do registro.   
@app.delete("/students/{id_student}")
async def delete_student(id_student: int):
    if id_student in list_registry_all_students:
        del list_registry_all_students[id_student]
        return f"Delete with sucess"
    else:
        return "not possible find ID"


if __name__ == "__main__":
    import uvicorn  # type: ignore
    uvicorn.run(app, host="127.0.0.1", port=8080, debug=True, reload=True)

