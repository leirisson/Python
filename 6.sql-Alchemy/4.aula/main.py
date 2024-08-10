from infra_config.repository.filmes_repository import FilmeRepositorio

repo = FilmeRepositorio()



# exibindo dados do banco
def exibindo_dados():
    data = repo.select()
    for dados in data:
        print(dados)

# inserindo dados do banco de dados 
def inserindo_dados():
    titulo = input("qual o titulo do filme: ")
    genero = input("qual o genero do filme: ")
    ano = int(input("qual o ano do filme: "))

    repo.insert_dados(titulo, genero, ano)
# ======================================================

#atualizando dados 
def atualizando_dados():
    print("atualizando dados")
    titulo = input("qual o titulo do filme: ")
    ano = int(input("qual o ano do filme: "))
    repo.atualizar(titulo, ano)
#===========

#   deletando dados 
def deletando_um_dado():
    titulo = input("qual o titulo do filme: ")
    repo.deletar_dado(titulo)

deletando_um_dado()
exibindo_dados()