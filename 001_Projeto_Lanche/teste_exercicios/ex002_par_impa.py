def titulo_do_sistema():
    print("PAR OU IMPA")


def obter_valores():
    numero = int(input("Digite um valor: "))
    return numero

def comparando_valore(numero):
    if numero % 2 == 0:
        print("numero par")
    else:
        print("numero impa")


def main():
    titulo_do_sistema()
    comparando_valore(obter_valores())
    

if __name__ == "__main__":
    main()