from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
import math


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + '-' + self.telefone


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.SET(get_sentinel_user), )
    proprietario = models.ForeignKey(Pessoa, on_delete=models.SET(get_sentinel_user), )
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()

    def __str__(self):
        return self.placa + ' - ' + self.marca.nome


class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'Parametros Gerais'


class MovRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET(get_sentinel_user), )
    pago = models.BooleanField(default=False)

    def horas_total(self):
        return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)

    def total(self):
        return self.valor_hora * self.horas_total()

    def __str__(self):
        return self.veiculo.placa


class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET(get_sentinel_user), )
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.veiculo) + ' - ' + str(self.inicio)


class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.SET(get_sentinel_user), )
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.mensalista) + ' - ' + str(self.dt_pgto)
