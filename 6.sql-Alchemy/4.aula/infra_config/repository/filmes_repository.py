from infra_config.configs.conxao import DBConnect
from infra_config.entidades.filmes import Filmes


class FilmeRepositorio:
    # visualizando dados do banco de dados
    def select(self):
        with DBConnect() as db:
            data = db.session.query(Filmes).all()
            return data

    # inserindo dados no banco de dados    
    def insert_dados(self, titulo, genero,ano):
        with DBConnect() as db:
            data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
            db.session.add(data_insert)
            db.session.commit()
    
    # deletando dados do banco de dados
    def deletar_dado(self, titulo):
        with DBConnect() as db:
            db.session.query(Filmes).filter(Filmes.titulo==titulo).delete()
            db.session.commit()

    # atualizando dados no banco de dados
    def atualizar(self, titulo, ano):
        with DBConnect() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).update({"ano":ano})
            db.session.commit()
        
    