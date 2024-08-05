###########################################################################
# 10. Sistema de Reservas de Quartos de Hotel                             #
# Crie uma API para gerenciar reservas de quartos                         #
# em um hotel, com as seguintes funcionalidades:                          #
###########################################################################
# Create: Registrar uma nova reserva com:                                 #
#     1 - nome do cliente,                                                #
#     2 - número do quarto,                                               #
#     3 - data de check-in                                                #
#     4 - check-out.                                                      #
# Read: Listar todas as reservas feitas.                                  #
# Update: Atualizar informações da reserva (data de check-in, check-out). #
# Delete: Cancelar uma reserva.                                           #
###########################################################################

from fastapi import FastAPI # type: ignore
from fastapi import HTTPException # type: ignore
from fastapi import Response # type: ignore
from fastapi import Path # type: ignore
from fastapi import status # type: ignore

from models.modelReserva import Reserva


app = FastAPI()


data_list_reservation = {
    1: {
        "name_client": "Leirisson Souza",
        "number_of_room": 45,
        "data_check_in": "01/08/2024",
        "data_check_out": "05/08/2024"
    },
    2: {
        "name_client": "Maria Silva",
        "number_of_room": 12,
        "data_check_in": "05/08/2024",
        "data_check_out": "10/08/2024"
    },
    3: {
        "name_client": "João Pereira",
        "number_of_room": 23,
        "data_check_in": "10/08/2024",
        "data_check_out": "15/08/2024"
    },
    4: {
        "name_client": "Ana Souza",
        "number_of_room": 34,
        "data_check_in": "15/08/2024",
        "data_check_out": "20/08/2024"
    },
    5: {
        "name_client": "Carlos Santos",
        "number_of_room": 56,
        "data_check_in": "20/08/2024",
        "data_check_out": "25/08/2024"
    },
    6: {
        "name_client": "Fernanda Lima",
        "number_of_room": 78,
        "data_check_in": "25/08/2024",
        "data_check_out": "30/08/2024"
    }
}




@app.get("/")
async def index():
    return {"msg": " welcom to API "}

# Read: Listar todas as reservas feitas. 
@app.get("/reservation")
async def all_reservation():
    return data_list_reservation


@app.get("/reservation/{id_reservation}")
async def one_resrvation(id_reservation: int = Path(title="id da reservar", description="deve ser de 1 até 10", gt=0, lt=10)):
    try:
        reservation = data_list_reservation[id_reservation]
        return reservation
    except KeyError:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Curso não encontrado")


# Create: Registrar uma nova reserva
@app.post("/reservation")
async def create_new_reservetion(reservation : Reserva):
    next_id = len(data_list_reservation) + 1
    reservation.id = next_id
    
    if reservation.id not in data_list_reservation:
        data_list_reservation[reservation.id]  = reservation
        del reservation.id
        return f"created with sucess."
    else:
        return "not possible created"


# Update: Atualizar informações da reserva (data de check-in, check-out)
@app.patch("/reservation/{id_reservation}")
async def update_data_reservation(id_reservation: int, reservation: Reserva):
    if id_reservation in data_list_reservation:
        data_list_reservation[id_reservation].data_check_in = reservation.data_check_in
        data_list_reservation[id_reservation].data_check_out = reservation.data_check_out
        return f"update sucess."
    else:
        return f"ID not found: {id_reservation}"

# Delete: Cancelar uma reserva
@app.delete("/reservation/{id_reservation}")
async def delete_data_reservation(id_reservation: int):
    if id_reservation in data_list_reservation:
        del data_list_reservation[id_reservation]
        return "deleted with sucess"
    else:
        return f"not possible find id: {id_reservation}"
    
    
    
if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app, host="127.0.0.1", port=8080, debug=True, reload=True)