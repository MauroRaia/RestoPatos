from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from core.models import *
#Create your views here.

class Home(View):

    def get(self, request):

        return render(request, 'home.html', {"cuenta" : "5"})




