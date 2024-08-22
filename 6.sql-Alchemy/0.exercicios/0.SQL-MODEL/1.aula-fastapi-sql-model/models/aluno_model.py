from typing import Optional

from sqlmodel import Field, SQLModel # type: ignore


class Aluno_model(SQLModel, table=True):
    __tablename__: str = "alunos"

    id: Optional[int] =  Field(default=None, primary_key=True)
    nome: str
    turma: str
    idade: int 