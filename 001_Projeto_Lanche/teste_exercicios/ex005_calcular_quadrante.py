#Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e
#utilize uma estrutura if elif else para determinar em qual quadrante 
#do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

import os
def exibir_titulo():
    os.system("cls")
    titulo = "Sistema de quadrante"
    print(len(titulo) * "=")
    print(titulo)
    print(len(titulo) * "=")

def coletar_dados():

    valor_de_x = float(input("informe o valor de x: "))
    valor_de_y = float(input("informe o valor de y "))
    
    if valor_de_x > 0 and valor_de_y > 0:
        print(f"cordenada {valor_de_x},{valor_de_y} esta o primeiro quadrante")
    elif(valor_de_x < 0 and valor_de_y > 0):
        print(f"A cordenada {valor_de_x}, {valor_de_y} esta no segundo quadrante")
    elif(valor_de_x < 0 and valor_de_y < 0):
        print(f"A cordenada {valor_de_x},{valor_de_y} esta no terceiro quadrante")
    elif valor_de_x > 0 and valor_de_y < 0:
        print("A cordenada esta no quarto quadrante")
    else:
        print("o ponto está localizado no eixo ou origem.")

def main():
    exibir_titulo()
    coletar_dados()


if __name__ == "__main__":
    main()
