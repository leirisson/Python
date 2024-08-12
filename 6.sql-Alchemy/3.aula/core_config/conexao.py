from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DB_connect:
    def __init__(self) -> None:
        self.__string_de_coneccao = "postgresql://postgres:123456@localhost:5432/cadastro"
        self.__engine = self.create_database_engine()
        self.session = None

    def create_database_engine(self):
        engine = create_engine(self.__string_de_coneccao)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
    