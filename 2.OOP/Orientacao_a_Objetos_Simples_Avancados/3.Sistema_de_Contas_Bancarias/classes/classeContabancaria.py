class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, saldo):
        self.saldo += saldo
        return self.saldo
    
    def sacar(self, valor_saque):
        if valor_saque < self.saldo:
            return f"Saque do valor {valor_saque} realizado com sucesso. Saldo atual: {self.saldo}"
        return "Saldo insuficiente para realizar saque."
    