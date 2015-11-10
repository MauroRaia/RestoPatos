from django.db import models


class Mesa(models.Model):
    numero = models.IntegerField()
    cobrado = models.BooleanField(default=True)

class Carta(models.Model):
    nombre = models.CharField(max_length=100, default="Carta principal")
    precio_actual = models.IntegerField(default=0, editable=False, null=True)
    seccion_actual = models.ForeignKey("Seccion", null=True, blank=True)

    def __unicode__(self):
        return self.nombre

class Pedido(models.Model):
    Ordenado = "El plato esta por ser elaborado"
    Cocinando = "Elaborando el plato"
    Pagado = "Plato cobrado"
    estados_platos = (
        (Ordenado, "Ordenado"),
        (Cocinando, "Cocinando"),
        (Pagado, "Pagado")
        )
    mesa = models.ForeignKey("Mesa")
    platos = models.ForeignKey("Plato")
    fecha = models.DateField(auto_now_add=True)
    estados = models.CharField(max_length=1, choices=estados_platos, default="Pedido")

class Valoracion(models.Model):
    fecha = models.DateField()
    valor_plato = models.DecimalField(default=0.0, decimal_places=1, max_digits=2)
    plato_valorado = models.ForeignKey("Plato")

class Plato(models.Model):
    precio = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    nombre = models.CharField(max_length=100)
    valor_total = models.DecimalField(default=0.0, decimal_places=1, max_digits=2)
    seccion_platos = models.ForeignKey("Seccion", null=True)

    def precio_display(self):
        return '${0}'.format(self.precio)

    def __unicode__(self):
        return self.nombre + " / $" + str(self.precio)


class Bebida(models.Model):
    precio = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    nombre = models.CharField(max_length=100)
    seccion_bebida = models.ForeignKey("Seccion", null=True)

    def precio_display(self):
        return '${0}'.format(self.precio)

    def __unicode__(self):
        return self.nombre + " / $" + str(self.precio)


class Seccion(models.Model):
    nombre = models.CharField(max_length=100)
    carta_seccion = models.ForeignKey("Carta", null=True)
