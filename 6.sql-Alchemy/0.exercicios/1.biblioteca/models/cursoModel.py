from infra_config.configs import settings

from sqlalchemy import column, Integer, String


class CursoModel(settings.BD_base_model):
    __tablename__ = "cursos"

    id: int = column(Integer, primary_key = True, autoincrement=True)
    titulo: str = column(String(100))
    aulas: int = column(Integer)
    horas: int = column(Integer)


