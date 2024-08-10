
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, String, Integer


# criando configurações
engine = create_engine("postgresql://postgres:123456@localhost:5432/cinema")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
conexao = engine.connect()

#Entidade 
class Filmes(Base):
    __tablename__ = "filmes"

    #colunas da tebelas do banco de dados
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme: titulo={self.titulo}, ano={self.ano}"
    

# interagindo com o banco de dados


# #INSERT
print("Cadastrar Filmes")
nome_do_filme = input("Nome do filme: ")
genero_do_filme = input("Genero do filme: ")
ano_do_filme = int(input("Ano: "))

data_insert = Filmes(titulo=nome_do_filme, genero=genero_do_filme, ano=ano_do_filme)
# Adicionando o novo registro à sessão
session.add(data_insert)
# Persistindo (inserindo) no banco de dados
session.commit()
# Fechando a sessão
session.close()


# UPDATE
update_filme = input("atualizar filme por genero: ")
session.query(Filmes).filter(Filmes.genero == update_filme).update({"ano":1999})
session.commit()
session.close()


#DELETE
deletar_filme = input("Deletar, Nome do filme: ")
session.query(Filmes).filter(Filmes.titulo==deletar_filme).delete()
session.commit()
session.close()

#SELECT
data = session.query(Filmes).all()
for filme in data:
    print(filme)
