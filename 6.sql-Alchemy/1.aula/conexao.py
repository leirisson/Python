from sqlalchemy import create_engine # type: ignore
from sqlalchemy import text

# engine = create_engine("mysql+pymysql://root:123456@localhost:3307/cinema")
engine = create_engine("postgresql://postgres:123456@localhost:5432/cinema")


conexao = engine.connect()

consulta_sql = text("SELECT * FROM filmes;")

response = conexao.execute(consulta_sql)


lista_de_filmes = []
for row in response:
    lista_de_filmes.append(row.titulo)


print(lista_de_filmes)


conexao.close()
print("conexao fechada")

