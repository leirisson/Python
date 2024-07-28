from classes.classeVeiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

    def exibir_informacoes(self):
        informacoes = f"marca: {self.marca} | ano: {self.ano} | cilindradas: {self.cilindradas}".upper()
        return informacoes
    
    def exibir_cilindradas(self):
        return self.cilindradas
    
