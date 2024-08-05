

from models.modelBaseEntity import BaseEntity

class Task(BaseEntity):
    description : str
    date : str
    status: str
    id_user : str
    id_project : str
    