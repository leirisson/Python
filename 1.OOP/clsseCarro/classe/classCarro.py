from datetime import datetime


class Carro:
    total_carros  = 0

    def __init__(self, marca, modelo, ano):
        
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        Carro.total_carros +=  1
    
    # forma metodo amigavel de exibição das informações 
    def __str__(self):
        return f"{self.__marca}  {self.__modelo}  {self.__ano}"

    def exibir_informacoes(self):
        info = f"""marca: {self.__marca} - modelo: {self.__modelo} - ano: {self.__ano}""".upper()
        return info
    
    
    def atualizar_ano(self, novo_ano):
        self.__ano = novo_ano
        print("Ano atualizado com sucesso.")
        return self.__ano
    
    def get_marca(self):
        return self.__marca
    
    def set_marca(self, nova_marca):
        self.__marca = nova_marca
        
    def get_ano(self):
        return self.__ano
    
    def set_ano(self, novo_ano):
        self.__ano = novo_ano
    
    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    @staticmethod
    def carro_antigo(ano):

        estado = False

        if ano < 2000:
            estado = True
        
        return estado
    def exibir_total_de_carros(self):
        print(f"Total de carros cadastrados: {Carro.total_carros}")
    
    #verificando se o objeto carro tem o  mesmo  ano
    # retorna True se sim ou se for False se não 
    def __eq__(self, other):
        if isinstance(other, Carro):
            return self.__ano == other.__ano
        return False
    
    # retornando a idade do carro com base no ano atual
    def idade_do_carro(self):
        dataAtual = datetime.now()
        ano_atual = dataAtual.year

        idade_carro = ano_atual - self.__ano

        return f"idade do carro: {idade_carro}"