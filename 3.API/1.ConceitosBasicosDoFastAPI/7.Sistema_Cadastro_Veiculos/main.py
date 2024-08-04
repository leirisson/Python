####################################################################
# 8. Sistema de Cadastro de Veículos                               #
# Crie uma API para gerenciar o cadastro de                        #
# veículos de uma concessionária, com as seguintes funcionalidades:#
####################################################################
# Create: Adicionar um novo veículo com:                           #
# 1 - marca                                                        #
# 2 - modelo                                                       #
# 3 - ano                                                          #
# 4 - preço.                                                       #
# Read: Listar todos os veículos cadastrados.                      #
# Update: Atualizar informações do veículo (preço).                #
# Delete: Remover um veículo do cadastro.                          #
####################################################################

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from models.modelVeiculo import Vehicle

app = FastAPI()

list_registry_vehicle = {
    1: {
        "brand": "Ferrari",
        "model": "Diablo 2000",
        "year": "2005",
        "price": 1000000.56
    },
    2: {
        "brand": "Lamborghini",
        "model": "Aventador",
        "year": "2018",
        "price": 1500000.75
    },
    3: {
        "brand": "Porsche",
        "model": "911 Carrera",
        "year": "2020",
        "price": 1200000.30
    },
    4: {
        "brand": "Bugatti",
        "model": "Chiron",
        "year": "2019",
        "price": 3000000.00
    },
    5: {
        "brand": "McLaren",
        "model": "P1",
        "year": "2015",
        "price": 2000000.45
    },
    6: {
        "brand": "Tesla",
        "model": "Model S",
        "year": "2021",
        "price": 800000.50
    }
}


@app.get("/")
async def index_api():
    return {"msg":"Hello wellcom to API register for VEHICLE."}

# Read: Listar todos os veículos cadastrados.
@app.get("/registry")
async def all_registry_vehicle():
    return list_registry_vehicle


# Create: Adicionar um novo veículo
@app.post("/registry")
async def create_new_registry(vehicle: Vehicle):
    next_id = len(list_registry_vehicle) + 1
    vehicle.id = next_id
    
    if vehicle.id not in list_registry_vehicle:
        list_registry_vehicle[vehicle.id] = vehicle
        del vehicle.id
        return f"sucess create new registry ID: {next_id}" 
    else:
        # faliure => falha
        return "Faliure in create new registry."

# Update: Atualizar informações do veículo
@app.patch("/registry/{id_registry}")
async def update_registry(id_registry: int, vehicle: Vehicle):
    if id_registry in list_registry_vehicle:
        list_registry_vehicle[id_registry].price = vehicle.price
        return f"sucess in the update."
    else:
        return "not is possible realize update."
    
    
    
# Delete: Remover um veículo do cadastro.   
@app.delete("/registry/{id_registry}")
async def delete_registry(id_registry: int):
    if id_registry in list_registry_vehicle:
        del list_registry_vehicle[id_registry]
        return "register delete with sucess."
    else:
        return "register not delete."
    
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080, debug=True, reload=True)
    