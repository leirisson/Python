class Usuario:
    def __init__(self, nome, id) -> None:
        self.nome = nome
        self.id = id
        self.lista_de_emprestimos = []

    

    def emprestar(self, objeto):
        if objeto.disponibilidade == True:
            self.lista_de_emprestimos.append(objeto)
        else:
            return "Este livro não esta disponivel para emprestimo."
            
        return "Livro cadastrado com sucesso."
    
    def devolver(self, titulo):
        for emprestimo in self.lista_de_emprestimos:
            if titulo == emprestimo.titulo:
                self.lista_de_emprestimos.remove(emprestimo)
                break
        return "Livro devolvido com sucesso."
    
    def exibir_emprestimos(self):
        contador_livro = 0
        for emprestimo in self.lista_de_emprestimos:
            contador_livro += 1
            print(f"{contador_livro}: {emprestimo}")
        return "livros emprestados."

