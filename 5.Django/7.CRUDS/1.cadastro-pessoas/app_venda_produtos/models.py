from django.db import models

# classe de cadastro de cliente
class Cadastro_cliente(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    sobrenome = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)


# classe de cadastro de marcas
class Cadastro_marca(models.Model):
    nome_marca = models.CharField(max_length=20, blank=False, null=False)


# classe de cadastro de produto
class Cadastro_de_produto(models.Model):
    codigo = models.CharField(max_length=20, blank=False, null=False, unique=True)
    descricao = models.CharField(max_length=100, blank=False, null=False)
    marca = models.ForeignKey(Cadastro_marca, on_delete=models.PROTECT)
    custo = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    preco_venda = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)



# classe de vendas
class Vendas(models.Model):
    cliente = models.ForeignKey(Cadastro_cliente, on_delete=models.PROTECT)
    produto = models.ForeignKey(Cadastro_de_produto, on_delete=models.PROTECT)
    valor_tootal = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)

