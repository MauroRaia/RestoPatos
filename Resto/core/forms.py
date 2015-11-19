from django import forms
from django.forms import ModelForm
from .models import Pedido

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
