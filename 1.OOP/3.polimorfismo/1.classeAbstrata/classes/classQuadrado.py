from classes.classeForma import Forma

class Quadrado(Forma):
    def __init__(self,lado):
        self.lado = lado
        
        

    def calcular_forma(self):
        cal = pow(self.lado, 2)
        return cal