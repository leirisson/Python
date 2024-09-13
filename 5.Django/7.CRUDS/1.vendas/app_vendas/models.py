from django.db import models

# Create your models here.
class Cadastro_cliente(models.Model):
    nome = models.CharField(max_length=25, blank=False, null=False)
    sobre_nome = models.CharField(max_length=25, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, unique=True, null=False)
    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return self.nome

class Cadastro_marca(models.Model):
    nome = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self) -> str:
        return self.nome

class Cadastro_produto(models.Model):
    codigo = models.CharField(max_length=6, unique=True, blank=False, null=False)
    nome = models.CharField(max_length=20, blank=True, null=True)
    descricao = models.CharField(max_length=60, blank=False, null=False)
    marca = models.ForeignKey(Cadastro_marca, on_delete=models.CASCADE)
    custo =  models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    preco_vendas = models.DecimalField(max_digits=8, decimal_places= 2, blank=False, null=False)

    def __str__(self):
        return self.codigo

class Cadastro_vendas(models.Model):
    cliente = models.ForeignKey(Cadastro_cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Cadastro_produto, on_delete=models.CASCADE)
    total_compra = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)

    
