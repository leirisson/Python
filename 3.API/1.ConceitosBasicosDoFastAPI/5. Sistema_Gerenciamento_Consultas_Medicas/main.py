from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from models.modelConsulta import Consulta


consultas_medicas = {
    1: {
        "nome_cliente": "Leirisson Souza",
        "nome_medico": "Dra. Maria da Silva",
        "data_consulta": "20/08/2024",
        "hora_consulta": "17:00:00"
    },
    2: {
        "nome_cliente": "Ana Oliveira",
        "nome_medico": "Dr. João Pedro",
        "data_consulta": "21/08/2024",
        "hora_consulta": "10:00:00"
    },
    3: {
        "nome_cliente": "Carlos Ferreira",
        "nome_medico": "Dra. Beatriz Nunes",
        "data_consulta": "22/08/2024",
        "hora_consulta": "14:00:00"
    },
    4: {
        "nome_cliente": "Mariana Lima",
        "nome_medico": "Dr. Ricardo Mendes",
        "data_consulta": "23/08/2024",
        "hora_consulta": "09:00:00"
    },
    5: {
        "nome_cliente": "Felipe Costa",
        "nome_medico": "Dra. Juliana Alves",
        "data_consulta": "24/08/2024",
        "hora_consulta": "11:30:00"
    },
    6: {
        "nome_cliente": "João Silva",
        "nome_medico": "Dr. Roberto Andrade",
        "data_consulta": "25/08/2024",
        "hora_consulta": "08:00:00"
    },
    7: {
        "nome_cliente": "Fernanda Souza",
        "nome_medico": "Dra. Clara Lima",
        "data_consulta": "26/08/2024",
        "hora_consulta": "13:00:00"
    },
    8: {
        "nome_cliente": "Ricardo Pereira",
        "nome_medico": "Dr. Paulo Santos",
        "data_consulta": "27/08/2024",
        "hora_consulta": "15:00:00"
    },
    9: {
        "nome_cliente": "Aline Martins",
        "nome_medico": "Dra. Patrícia Rocha",
        "data_consulta": "28/08/2024",
        "hora_consulta": "12:00:00"
    },
    10: {
        "nome_cliente": "Bruno Gomes",
        "nome_medico": "Dr. Fernando Silva",
        "data_consulta": "29/08/2024",
        "hora_consulta": "16:30:00"
    }
}


app  = FastAPI()

@app.get("/")
async def index():
    return { "msg" : "boas vindas a API de consulta"}

# Listar todas as consultas agendadas.
@app.get("/consultas")
async def get_sonsultas():
    return consultas_medicas

#  Marcar uma nova consulta com nome do paciente, nome do médico, data e hora da consulta.
@app.post("/consultas")
async def criar_consulta(consulta: Consulta):
    proximo_id = len(consultas_medicas) + 1
    consulta.id = proximo_id

    try:

        if consulta.id not in consultas_medicas:
            consultas_medicas[consulta.id] = consulta
            del consulta.id
            return "consulta agendada com sucesso."
        
    except KeyError as e:
        raise f"Erro ao marca consulta {e}"


@app.patch("/consultas/{id_consulta}")
async def editar_consulta(id_consulta: int, consulta: Consulta):
    try:
        if id_consulta in consultas_medicas:
            consultas_medicas[id_consulta].data_consulta = consulta.data_consulta
            consultas_medicas[id_consulta].hora_consulta = consulta.hora_consulta
            return f"{consultas_medicas[id_consulta].data_consulta} e {consultas_medicas[id_consulta].hora_consulta}, atualizado."
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="A consulta não foi encontrada.")
    except KeyError as e:
        raise f"Eror ao tentar atualizar consulta => {e}"


#  Cancelar uma consulta
@app.delete("/consultas/{id_consulta}")
async def deletar_consulta(id_consulta: int):
   
    if id_consulta in consultas_medicas:
            print(consultas_medicas[id_consulta])
            del consultas_medicas[id_consulta]
            return "consulta deletada."
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consulta não encontrada.")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080, debug=True, reload=True)

    