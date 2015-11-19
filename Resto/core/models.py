from django.db import models

class Tablet(models.Model):
    id_interno = models.IntegerField()
    id_mesa = models.ForeignKey("Mesa", blank=True)

    def __unicode__(self):
        return str(self.id_interno) + " / " + str(self.id_mesa)

class Mesa(models.Model):
    numero = models.IntegerField()

    def __unicode__(self):
        return "Numero de mesa: " + str(self.numero)

class Carta(models.Model):
    nombre = models.CharField(max_length=100, default="Carta principal")

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
    platos = models.ForeignKey("Plato", blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    estados = models.CharField(max_length=1, choices=estados_platos, default="Pedido")
    precio_actual = models.IntegerField(default=0, editable=False, null=True)
    seccion_actual = models.ForeignKey("Seccion", null=True, blank=True)
    cobrado = models.BooleanField(default=False)



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
        return self.nombre + " / $" + str(self.precio) + " / Seccion: " + str(self.seccion_platos)


class Sin_Alcohol(models.Model):
    precio = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    nombre = models.CharField(max_length=100)
    seccion_bebida = models.ForeignKey("Seccion", null=True)

    def precio_display(self):
        return '${0}'.format(self.precio)

    def __unicode__(self):
        return self.nombre + " / $" + str(self.precio) + " / Seccion: " + str(self.seccion_bebida)


class Seccion(models.Model):
    nombre = models.CharField(max_length=100)
    carta_seccion = models.ForeignKey("Carta", null=True)
    id_seccion = models.IntegerField(null=True)

    def __unicode__(self):
        return self.nombre
