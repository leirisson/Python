from infra_config.configs import settings

from sqlalchemy import Column, Integer, String


class CursoModel(settings.BD_base_model):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key = True, autoincrement=True)
    titulo = Column(String(100))
    aulas = Column(Integer)
    horas = Column(Integer)


