from django.db import models


class Empresa(models.Model):
    mome = models.CharField(max_length=100, help_text="Nome da Empresa")
