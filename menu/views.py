from django.shortcuts import render
from django.http import HttpResponse


# / menu
def index(request):
    return HttpResponse("Bienvenue sur le Menu du restaurant")
# Create your views here.
