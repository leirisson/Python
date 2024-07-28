from classes.classCachorro import Cachorro
from classes.classGato import Gato


def main():

    scoob = Cachorro("scoob","cachorro")
    bigode = Gato("bigode", "gato")

    
    # lista_de_objetos = [scoob, bigode]

    # for animal in lista_de_objetos:
    #     print(animal.fazer_som())

    def executar_som(animal):
       print(animal.fazer_som())
        
    executar_som(scoob)
    executar_som(bigode)

    def especie_unica(animal):
        if animal.especie == 'gato':
            print(animal.escalar())
        else:
            print(animal.correr())

    especie_unica(scoob)
    especie_unica(bigode)

if __name__ == "__main__":
    main()