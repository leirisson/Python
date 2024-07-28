# Crie uma classe Produto com atributos nome, preco e quantidade.
# Adicione métodos para aumentar e diminuir a quantidade.
# Crie uma classe Inventario que gerencia uma lista de produtos, incluindo métodos para adicionar,
# remover e listar produtos, bem como calcular o valor total do inventário.

from classes.classeProduto import Produto
from classes.classeInventario import Inventario


def main():
    nome = input("Qual o nome do produto: ")
    preco = float(input("qual o preço do produto: "))
    quantidade = int(input("qual a quantidade: "))


    teclado = Produto(nome, preco, quantidade)
    teclado1 = Produto(nome, preco, quantidade)
    teclado2 = Produto(nome, preco, quantidade)

    print(teclado.aumentar_produto(nome,quantidade))
    print(teclado1.diminuir_produto(nome,quantidade))

    inventario_estoque = Inventario()
    inventario_estoque.adcionarProdutos(teclado)
    inventario_estoque.adcionarProdutos(teclado1)
    inventario_estoque.adcionarProdutos(teclado2)

    inventario_estoque.listar_produtos_cadastrados()
    print(inventario_estoque.calc_valor_total_inventario())

    
if __name__ == "__main__":
    main()