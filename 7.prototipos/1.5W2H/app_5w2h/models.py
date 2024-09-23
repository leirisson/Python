from django.db import models

# Create your models here.

class Strategy(models.Model):
    name = models.CharField(max_length=30, blank=True) # nome da estrategia
    what = models.CharField(max_length=30, blank=False) # what: O que será feito.
    why = models.TextField() # why: Por que será feito.
    where = models.CharField(max_length=60, blank=False) # Onde será feito.
    when = models.DateField() # Quando será feito.
    who = models.CharField(max_length=30, blank=False) # Quem irá fazer
    how = models.TextField() # Como será feito.
    how_much = models.DecimalField(max_digits=8, decimal_places=2) #Quanto vai custar.

    def __str__(self):
        return self.name
    