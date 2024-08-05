class Livro:
    def __init__(self, titulo, autor, isbn, disponibilidade):
        self.titulo = titulo
        self.autor = autor 
        self.isbn = isbn
        self.disponibilidade = disponibilidade
    
    def __str__(self) -> str:
        if self.disponibilidade == True:
            return f"{self.titulo} | {self.autor} | {self.isbn} | disponivel".upper()
        return f"{self.titulo} | {self.autor} | {self.isbn} | emprestado".upper()
    
