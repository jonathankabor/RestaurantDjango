from django.shortcuts import render
from django.http import HttpResponse
from .models import Burger


# / menu
def index(request):
    Burgers = Burger.objects.all()
    Burgers_list = ','.join([str(burger) + " : " + str(burger.prix) + "€" for burger in Burgers])
    return HttpResponse(f"Bienvenue sur le Menu du restaurant. Burgers disponibles : {Burgers_list}")
# Create your views here.
