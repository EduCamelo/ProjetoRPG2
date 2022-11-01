from django.db import models
from .Person import *

class Personagem1(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(max_length=200)
    classe_Person = models.CharField(max_length=10, choices=classes.choices, default=0)
    destino = models.CharField(max_length=10, choices=Destino.choices, default=0)
    