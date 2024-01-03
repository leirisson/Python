#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura 
#if elif else para classificar a idade em categorias de acordo com as seguintes condições:

#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.


import os

def exibir_titulo():
    os.system("cls")
    nome_do_siatema = "Idade do Aluno"
    print(len(nome_do_siatema) * "=")
    print(nome_do_siatema)
    print(len(nome_do_siatema) * "=")

def obter_dados_do_aluno():
    idade_aluno = int(input("qual sua idade: "))
    return idade_aluno

def classificando_aluno(idade_aluno):
    if idade_aluno == 0 or idade_aluno <= 12:
        print("Este aluno é uma criança") 

def main():
    exibir_titulo()
    classificando_aluno(obter_dados_do_aluno())


if __name__ == "__main__":
    main()