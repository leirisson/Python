from classes.classeMoto import Moto
from classes.classeCaminhao import Caminhao
from classes.classeAnfibio import Anfibio
# marca = input("Qual a marca da moto: ")
# cilindradas = int(input("Qual a cilindradas da moto: "))
# ano = int(input("Qual o ano de lançamento da moto: "))

# biz125 = Moto(marca, ano, cilindradas)

# exibir informações da moto
# print(biz125.exibir_informacoes())
# print(biz125.exibir_cilindradas())


# ==================================================================

marca = input("Qual a marca da caminhão: ")
cilindradas = int(input("Qual a cilindradas da caminhão: "))
carga = float(input("Qual a capacidade de carga: "))
nivel_de_combustivel = float(input("qual o nivel de combustivel: "))

caminhao_volvo = Caminhao(marca, cilindradas, carga, nivel_de_combustivel)


# exibir informações do caminhão
print(caminhao_volvo.exibir_informacoes())
print(caminhao_volvo.rodar())
# ===================================================================

# tipo = input("Qual tipo do veiculo: ")
# tamanho = float(input("qual o tamanho do veiculo: "))
# marca = input("Qual a marca: ")
# ano = int(input("Qual o ano do veiculo: "))
# buzinar = input("Biznar ?: ")


# carro_lancha = Anfibio(tipo, tamanho, marca, ano, buzinar)

# print(carro_lancha.rodar())
