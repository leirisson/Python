class Inventario:
    def __init__(self):
        self.lista_de_produtos = []


    def __str__(self):
        return self.lista_de_produtos

    def adcionarProdutos(self, produto):
        self.lista_de_produtos.append(produto)
        return "produto adcionado com sucesso."
    
    #remover um produto do estoque 
    def remover_produto(self, produto):
        for p in self.lista_de_produtos:
            if produto.nome == p.nome:
                self.lista_de_produtos.remove(p)

    def calc_valor_total_inventario(self):
        valor_total = 0
        for produto in self.lista_de_produtos:
            if produto.quantidade > 0:
                valor_total += produto.quantidade * produto.preco
        return valor_total

    def listar_produtos_cadastrados(self):
        for produto in self.lista_de_produtos:
            print(f"Nome: {produto.nome} | preço: {produto.preco} | quantidade: {produto.quantidade}")
        