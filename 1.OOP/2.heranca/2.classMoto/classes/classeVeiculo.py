

class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
    
    def __str__(self) -> str:
        return f"{self.marca} {self.ano}"
    
    def exibir_informacoes(self):
        informacoes = f"marca: {self.marca} | ano: {self.ano}"
        return informacoes
    
    def rodar(self):
        return "rodanddo...".upper()