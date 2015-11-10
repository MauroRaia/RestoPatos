from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Mesa)
admin.site.register(Carta)
admin.site.register(Pedido)
admin.site.register(Valoracion)
admin.site.register(Plato)
admin.site.register(Bebida)
admin.site.register(Seccion)