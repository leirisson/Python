


class Veiculo:
    def __init__(self, marca, ano):
        self.__marca = marca
        self.__ano = ano


    def __str__(self) -> str:
        return f"{self.__marca} {self.__ano}"
    
    def get_marca(self):
        return self.__marca

    def get_ano(self):
        return self.__ano

    def exibir_informacoes(self):
        return f"marca: {self.__marca} | ano: {self.__ano}".upper()
    
     