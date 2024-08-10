from repository.cadastros_repository import Cadastros_repositorio

repo = Cadastros_repositorio()


#exibindo dados do usuario
def exibir_todos_cadastros():
    data_cadastro = repo.select()
    for cadastro in data_cadastro:
        print(cadastro)





exibir_todos_cadastros()