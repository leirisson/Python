from django.contrib import admin
from app_vendas import models

# Register your models here.

admin.site.register(models.Cadastro_cliente)
admin.site.register(models.Cadastro_marca)
admin.site.register(models.Cadastro_produto)
admin.site.register(models.Cadastro_vendas)
