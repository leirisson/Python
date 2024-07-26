from classBiblioteca import Biblioteca
from classLivro import Livro

def main():
    biblioteca_manaus = Biblioteca()

    titulo = input("qual titulo do livro: ").upper()
    autor = input("Qual o autor do livro: ").upper()
    ano_lancamento = int(input("Qual o ano de laçamento: "))

    livro_c1 = Livro(titulo, autor, ano_lancamento)

    biblioteca_manaus.adcionar_livro(livro_c1)
    biblioteca_manaus.listar_todos_os_livros()

if __name__ == "__main__":
    main()