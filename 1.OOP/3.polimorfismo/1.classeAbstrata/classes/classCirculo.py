from classes.classeForma import Forma

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio 

    def calcular_forma(self):
        pi = 3.14
        cal = 2 * (self.raio * pi)
        return cal
    