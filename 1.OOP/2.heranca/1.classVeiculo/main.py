from classes.classeCarro import Carro


marca = input("qual a marca do carro: ")
ano = int(input("qual o ano do carro: "))
cilindradas = int(input("qual a cilindrada do carro: "))

carro1 = Carro(marca, ano, cilindradas)


print(carro1.exibir_informacoes())