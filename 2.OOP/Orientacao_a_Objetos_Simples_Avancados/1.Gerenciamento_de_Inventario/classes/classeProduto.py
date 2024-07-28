

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.produto = {'nome':self.nome, 'preco':self.preco, 'quantidade':self.quantidade}
        self.produtos = []
        self.produtos.append(self.produto)

    def aumentar_produto(self, nome, quantidade):
        for produto in self.produtos:
            if nome == produto['nome']:
                self.quantidade += quantidade
                break
        return f"quantidade do produto adcionado com sucesso. quantidade: {quantidade}"
    

    
    def diminuir_produto(self, nome, quantidade):
        for produto in self.produtos:
            if nome == produto['nome']:
                self.quantidade -= quantidade
                break
        return "Quantidade do produto atualizada com sucesso."




