class Revista:
    def __init__(self, titulo, editora, numero, disponibilidade):
        self.titulo = titulo
        self.editora = editora
        self.numero = numero
        self.disponibilidade = disponibilidade
    
    def __str__(self) -> str:
        if self.disponibilidade == True:
            return f"{self.titulo} | {self.editora} | {self.numero} | disponivel".upper()
        return f"{self.titulo} | {self.editora} | {self.numero} | emprestado".upper()
    