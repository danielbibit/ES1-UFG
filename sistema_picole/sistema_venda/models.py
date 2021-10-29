from django.db import models
from django.db.models.lookups import PostgresOperatorLookup
from django.db.models.query import prefetch_related_objects

class Picole(models.Model):
    marca = models.CharField(max_length=100)
    sabor = models.CharField(max_length=100)
    calorias = models.IntegerField()
    peso = models.FloatField()
    temperatura_ideal = models.IntegerField()


class Lote(models.Model):
    picole = models.ForeignKey(Picole, on_delete=models.CASCADE)
    estoque = models.IntegerField()
    vendedor_origem = models.CharField(max_length=100)
    data_compra = models.DateField()
    data_validade = models.DateField()
    quantidade_picoles = models.IntegerField()
    preco_lote = models.FloatField()


class Vendas(models.Model):
    horario = models.DateField()
    preco = models.FloatField()
    local = models.CharField(max_length=100)
    metodo_pagamento = models.CharField(max_length=100)
    tipo_picole = models.ForeignKey(Picole, on_delete=models.CASCADE)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
