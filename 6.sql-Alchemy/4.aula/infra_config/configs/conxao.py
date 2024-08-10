from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# postgresql://postgres:123456@localhost:5432/cinema
# mysql+pymysql://root:123456@localhost:3307/cinema

class DBConnect:
    def __init__(self) -> None:
        self.__connection_string = "postgresql://postgres:123456@localhost:5432/cinema"
        self.__engine = self.__create_database_engine()
        self.session = None


    # metodo privado
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    

    def get_engine(self):
        return self.__engine
    


    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        