from classes.classesVeiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

    

    def exibir_informacoes(self):
        informacoes = f"marca: {self.get_marca()} | ano: {self.get_ano()} | cilindrada: {self.cilindradas}".upper()
        return informacoes
    

    