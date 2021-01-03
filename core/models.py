from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)


class Marca(models.Model):
    nome = models.CharField(max_length=50)


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.SET(get_sentinel_user), )
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()

