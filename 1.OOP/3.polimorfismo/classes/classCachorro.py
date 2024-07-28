from classes.classAnimal import Animal

class Cachorro(Animal):
    def __init__(self, nome, especie):
        super().__init__(nome, especie)
    
    def fazer_som(self):
        return f"{self.nome} está latindo."
    
    def correr(self):
        return f"{self.nome} - {self.especie} está correndo"