from django.shortcuts import render
from .models import *
from django.http import *
# Create your views here.
def inicio(Request,nombreJugador):
    jugador1=jugador.objects.get(nombre=nombreJugador)
    context = {
        'nombre': nombreJugador
    }
    return render(Request,"prueba.html",context)