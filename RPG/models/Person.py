from django.db import models
from django.utils.translation import gettext_lazy as _

class classes(models.TextChoices):
    GUERREIRO = 'Guerreiro', _('Guerreiro')
    MAGO = 'Mago', _('Mago')
    ARQUEIRO = 'Arqueiro', _('Arqueiro')
    NECROMANTE = 'Necromante', _('Necromante')

class Destino(models.TextChoices):
    GLORIA =  'Glória', _('Glória eterna')
    VINGANCA = 'Vingança', _('Vingança sem fim')
    AMOR = 'Amor', _('Um belo amor')
