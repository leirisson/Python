from classes.classAnimal import Animal


class Gato(Animal):
    def __init__(self, nome, especie):
        super().__init__(nome, especie)


    def fazer_som(self):
        return f"{self.nome}, miando MIAU MIAU MIAU"
    
    def escalar(self):
        return f"{self.nome} esta escalando."
    