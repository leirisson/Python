import mysql.connector
from mysql.connector import errorcode


db_config = {
    'user': 'root',
    'password': '123456',
    'port':'3307',
    'host': 'localhost',
    'database': 'gestao_veiculos_db'
}

class Conexao:

    def connectar_db():
        try:
            conn = mysql.connector.connect(**db_config)
            print("conectado")
            return conn
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo está errado com seu nome de usuário ou senha")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("O banco de dados não existe")
            else:
                print(err)
        return None
    def fechar_conexao():
        conn = mysql.connector.connect(**db_config)
        conn.close()
        print("conexao fechado.")

    def setup_database(nome_base):
        conn = Conexao.connectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {nome_base} (
id  INT AUTO_INCREMENT PRIMARY KEY,
modelo VARCHAR(255) NOT NULL,
marca VARCHAR(255) NOT NULL,
cor VARCHAR(50),
ano INT
)
""")
            print(f"Tabela {nome_base} criado com sucesso.")
            conn.commit()
            cursor.close()
            Conexao.fechar_conexao()

    def criar_veiculo(tabela, modelo, marca, cor, ano):
        conexao = Conexao.connectar_db()
        query = f"""
INSERT INTO {tabela} (modelo, marca, cor, ano)
VALUES ({modelo}, {marca}, {cor}, {ano})
"""
        if conexao:
            cursor = conexao.cursor()
            cursor.execute(query)
            conexao.commit()
            print("dados inseridos com sucesso")
            cursor.close()
            Conexao.fechar_conexao()
