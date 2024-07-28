from classes.classeBarco import Barco
from classes.classeVeiculo import Veiculo

class Anfibio(Barco, Veiculo):
    def __init__(self, tipo, tamanho, marca, ano, buzinar):
        Barco.__init__(tipo, tamanho)
        Veiculo.__init__(marca, ano)
        self.buzinar = buzinar

        


    def rodar(self):
         return f"o {self.tipo} da {self.marca} está {self.buzinar}.".upper()  
    
    def navegar(self):
         return Barco.navegar(self)