
from classe.classCarro import Carro

def main():

    marca = input("Qual a marca do carro: ")
    modelo = input("Qual o modelo do carro: ")
    ano = int(input("Qual o ano de lançamaneto do carro: "))



    v1 = Carro(marca, modelo, ano)
    v2 = Carro(marca, modelo, ano)
    v3  = Carro(marca, modelo, ano)
    
    # exibindo as informações do objeto
    print(v1.exibir_informacoes())

    # atualizando o ano de lançamento do objeto
    v1.atualizar_ano(2002)
    print(v1.exibir_informacoes())

    # usando o metodo set_ano => para atualizar o ano de lançamento
    v1.set_ano(2045)
    print(v1.exibir_informacoes())

    # verificando se o carro é antigo ou não  
    print(v1.carro_antigo(ano)) # se o carro for antigo o metodo retorna True, se não for a o metodo retorna False

    v1.exibir_total_de_carros()

    #comparando dois objetos se os objetos tem o mesmo ano
    print(v1 == v2)

    #verificando a idade do carro
    print(v2.idade_do_carro())


if __name__ == "__main__":
    main()