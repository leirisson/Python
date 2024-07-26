

class Biblioteca:
    def __init__(self):
        self.lista_de_livros = []

    def adcionar_livro(self,livro):
        self.lista_de_livros.append(livro)
        print("Livro cadastro com sucesso")
    
    def listar_todos_os_livros(self):
        for livro in self.lista_de_livros:
            print(livro)
        