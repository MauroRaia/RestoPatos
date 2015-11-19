from django.shortcuts import render
from django.views.generic import View
from core.models import *
from core.forms import *
#Create your views here.

class Home(View):

    def get(self, request):

        return render(request, 'home.html', {"cuenta" : "5"})

class DescansoView(View):

    def get(self, request):
        return render(request, 'descanso.html')

class CartaView(View):

#probar el form
    #def add(request):
        #if request.method == 'POST':
            #form = PedidoForm(request.POST)
            #if form.is_valid():
                #form.save()
    #return render(request, 'page.html', {
    #'form': AllocationPlanForm()
        #}
        #)

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


        return render(request, 'carta.html',
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

        return render(request, 'carta.html',
            {
            "seccion" : seccion_actual,
            "platos": platos,
            "bebidas" : bebidas,
            "siguiente" : siguiente,
            "anterior" : anterior
            }
        )


