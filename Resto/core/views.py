from django.shortcuts import render
from django.views.generic import View
from core.models import *
#Create your views here.

class Home(View):

    def get(self, request):

        return render(request, 'home.html', {"cuenta" : "5"})


class CartaView(View):


    def post(self, request, *args, **kwargs):

        seccion_actual = Seccion.objects.get(id_seccion=kwargs["seccion_show"])

        platos = Plato.objects.filter(seccion_platos=seccion_actual)
        bebidas = Sin_Alcohol.objects.filter(seccion_bebida=seccion_actual)

        if seccion_actual.id_seccion == 2:
            anterior = seccion_actual.id_seccion - 1
            siguiente = seccion_actual.id_seccion + 1
        else:
            anterior = seccion_actual.id_seccion - 1
            siguiente = seccion_actual.id_seccion + 1


        return render(request, 'carta_prueba.html',
            {
            "seccion" : seccion_actual,
            "platos": platos,
            "bebibas" : bebidas,
            "siguiente" : siguiente,
            "anterior" : anterior
            }
        )

    def get(self, request, *args, **kwargs):

        seccion_actual = Seccion.objects.get(id_seccion=kwargs["seccion_show"])

        platos = Plato.objects.filter(seccion_platos=seccion_actual)
        bebidas = Sin_Alcohol.objects.filter(seccion_bebida=seccion_actual)

        if seccion_actual.id_seccion == 2:
            anterior = seccion_actual.id_seccion - 1
            siguiente = seccion_actual.id_seccion + 1
        else:
            anterior = seccion_actual.id_seccion - 1
            siguiente = seccion_actual.id_seccion + 1

        return render(request, 'carta_prueba.html',
            {
            "seccion" : seccion_actual,
            "platos": platos,
            "bebidas" : bebidas,
            "siguiente" : siguiente,
            "anterior" : anterior
            }
        )

