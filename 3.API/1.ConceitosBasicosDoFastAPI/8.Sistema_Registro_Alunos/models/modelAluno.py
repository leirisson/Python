# ####################################################################
# Create: Registrar um novo aluno com:                               #
# 1 - nome  => name_student                                          #
# 2 - idade   => age                                                 #
# 3 - série    => school_grade                                       #
# 4 - turma.   => school_class                                       #
# Read: Listar todos os alunos registrados.                          #
# Update: Atualizar informações do aluno (série, turma).             #
# Delete: Remover um aluno do registro.                              #
# ####################################################################

from pydantic import BaseModel
from typing import Optional

class Aluno(BaseModel):
    id : Optional[int] = None
    name_student : str
    age : int
    school_grade : str
    school_class : str
    