from django.db import models


class Mesa(models.Model):
    numero = models.IntegerField()
    cobrado = models.BooleanField(default=True)
    pedidos = models.ManyToManyField("Consumo")

class Carta(models.Model):
    pedidos_actuales = models.ManyToManyField("Consumo", editable=False)
    precio_actual = models.IntegerField(default=0, editable=False)
    seccion_actual = models.ForeignKey("Seccion", null=True)

class Consumo(models.Model):
    seccionh = models.ForeignKey("Seccion")
    realizado = models.BooleanField(editable=False, verbose_name="Estado que indica si el plato fue realizado y enviado o no. Cambiar por el admin a False en el caso de no haberlo realizado y haberlo cambiado como tal.")

class Platos(models.Model):
    precio = models.IntegerField()
    nombre = models.CharField(max_length=50)


class Seccion(models.Model):
    items = models.ManyToManyField("Consumo")
    cartah = models.ForeignKey("Carta", null=True)
