import os
def exibir_nome():
    print(""" 
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def finalizando_app():
     os.system("cls")
     print("Finalizando APP")

def exibir_opcaoes():
    print("1 - Cadastrar Lanchonete")
    print("2 - Listar Restaurante")
    print("3 - Ativar Restaurante")
    print("4 - Sair")
    


def escolher_opcoes():
    opcao_escolhida = int(input("Escolha uma opção: "))
    if opcao_escolhida == 1:
        print("Cadastrar Restaurantes ")
    elif opcao_escolhida == 2:
        print("Listar restaurantes")
    elif opcao_escolhida == 3:
        print("Ativar Restaurante")
    else:
        finalizando_app()


def main():
    exibir_nome()
    exibir_opcaoes()
    escolher_opcoes()


if __name__ == "__main__":
    main()