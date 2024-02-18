from django.db import models

class Telefone(models.Model):
    numero = models.CharField(max_length=15)

