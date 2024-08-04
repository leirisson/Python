####################################################################
# Create: Adicionar um novo veículo com:                           #
# 1 - marca                                                        #
# 2 - modelo                                                       #
# 3 - ano                                                          #
# 4 - preço.                                                       #
####################################################################

from pydantic import BaseModel
from typing import Optional

class Vehicle(BaseModel):
    id : Optional[int] = None
    #marca => brand
    brand : str
    # modelo => model
    model : str
    # year
    year : str
    #preço => price
    price : float
    
    


