from sqlalchemy import create_engine # type: ignore


engine = create_engine("mysql/=pymysql://root:123456@localhost:3307/cinema")


if engine:
    print("conexão ocorreu com sucesso")