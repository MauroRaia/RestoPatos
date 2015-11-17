from django.shortcuts import render
from django.views.generic import View
from core.models import *
#Create your views here.

class Home(View):

    def get(self, request):

        return render(request, 'home.html', {"cuenta" : "5"})


class CartaView(View):

    def get_ip(self):
        return str([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])


    def get_mesa(self):
        my_ip = self.get_ip()
        lista_mesas = Mesa.objects.all()
        for m in lista_mesas:
            if m["ip"] == my_ip:
                return m

    def get(self, request):
        #pedido = Pedido.objects.create(
            #mesa=self.get_mesa()
            #)
        #pedido_seccion = Pedido.seccion_actual
        return render(request, 'carta_prueba.html',
        #{
        #"pedido_seccion" : pedido_seccion,
        #"pedido" : pedido
        #}
        )

