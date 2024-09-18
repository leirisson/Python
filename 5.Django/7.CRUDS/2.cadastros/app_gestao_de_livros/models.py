from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    autor = models.CharField(max_length=100, blank=False, null=False)
    quantidade_paginas = models.IntegerField()
    ano_publicacao = models.DateField()

    def __str__(self) -> str:
        return self.titulo