###########################################################################
# Create: Registrar uma nova reserva com:                                 #
#     1 - nome do cliente,                                                #
#     2 - número do quarto,                                               #
#     3 - data de check-in                                                #
#     4 - check-out.                                                      #
###########################################################################



from pydantic import BaseModel # type: ignore
from typing import Optional

class Reserva(BaseModel):
    id : Optional[int] = None
    name_client : str
    number_of_room : int
    data_check_in: str
    data_check_out : str
    