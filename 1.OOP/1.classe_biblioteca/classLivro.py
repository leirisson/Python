

class Livro:
    def __init__(self, titulo, autor, ano_lancamento):
        self.titulo = titulo
        self.autor = autor
        self.ano_lancamento = ano_lancamento

    def __str__(self):
        return f"titulo: {self.titulo} | Autor: {self.autor} | Ano de lançamento: {self.ano_lancamento}"