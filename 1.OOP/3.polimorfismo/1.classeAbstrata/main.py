from classes.classQuadrado import Quadrado
from classes.classCirculo import Circulo


def main():
    area_quadrato1 = Quadrado(10)
    circulo_perimetro1 = Circulo(10)

    print("area do quadrado: ",area_quadrato1.calcular_forma())
    print(f"Perimetro do circulo: {circulo_perimetro1.calcular_forma():.2f}")


if __name__ == "__main__":
    main()