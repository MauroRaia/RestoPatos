from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Mesa)
admin.site.register(Carta)
admin.site.register(Consumo)
admin.site.register(Platos)
admin.site.register(Seccion)