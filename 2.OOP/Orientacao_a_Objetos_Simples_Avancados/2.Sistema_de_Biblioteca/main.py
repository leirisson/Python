# Sistema de Biblioteca
# Crie classes Livro, Revista e Usuario.
# A classe Livro deve ter atributos como:
# titulo, autor, isbn e disponibilidade. 
# A classe Revista deve ter atributos como:
# titulo, editora, numero e disponibilidade.
# A classe Usuario deve ter atributos como:
# nome, id_usuario e uma lista de itens emprestados.
# Crie métodos para emprestar e devolver livros e revistas.

from classes.classeLivro import Livro
from classes.classeRevista import Revista
from classes.classeUsuario import Usuario


def main():
    livro1 = Livro("Inteligência Artificial", "Simone M S", "9798851301735", True)
    livro2 = Livro("Inteligência Artificial", "Simone M S", "9798851301735", False)
    livro3 = Livro("Inteligência Artificial", "Simone M S", "9798851301735", True)
    revista1 = Revista("VITÓRIA DUPLA", "Veja", "26", True)
    revista2 = Revista("VITÓRIA DUPLA", "Veja", "26", True)
    revista3 = Revista("VITÓRIA DUPLA", "Veja", "26", False)

    usuario1 = Usuario("leirisson",1)

    # emprestando livros
    print(usuario1.emprestar(livro2))
    print(usuario1.emprestar(livro1))
    print(usuario1.emprestar(livro3))


    #emprestando revistas
    print(usuario1.emprestar(revista1))
    print(usuario1.emprestar(revista2))
    print(usuario1.emprestar(revista3))

    #exibindo emprestimos do usurio
    print(usuario1.exibir_emprestimos())

    print(usuario1.devolver("Inteligência Artificial"))
    print(usuario1.exibir_emprestimos())






if __name__ == "__main__":
    main()