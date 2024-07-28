from classes.classeVeiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, ano, carga, nivel_de_combustivel):
        super().__init__(marca, ano)
        self.carga = carga
        self.__nivel_de_combustivel = nivel_de_combustivel

    def exibir_informacoes(self):
        return f"ano: {self.ano} | marca: {self.marca} | carga: {self.carga} | nivel_de_combustivel: {self.__nivel_de_combustivel}".upper()
    
    def rodar(self):
        return "Rodando a cidade".upper()
    
    def get_nivel_de_combustivel(self):
        return self.__nivel_de_combustivel
    
    def set_nivel_de_combustivel(self, novo_nivel_de_combustivel):
        self.__nivel_de_combustivel = novo_nivel_de_combustivel
    
