from core_config.conexao import DB_connect
from entidades.cadastros import Cadastros

class Cadastros_repositorio:
    def select(self):
        with DB_connect() as db:
            dados_do_banco = db.session.query(Cadastros).all()
            return dados_do_banco