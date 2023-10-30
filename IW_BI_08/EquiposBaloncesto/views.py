from django.shortcuts import render
from .models import *
from django.http import *
from django.template import *
# Create your views here.
def inicio(Request):
    categorias= categoria.objects.order_by('nombreCategoria')
    context = { 
        'categorias': categorias,
        }
    return render(Request,"prueba.html",context)

def vistacategoria(Request,nombre_Categoria):
    cat=categoria.objects.get(nombreCategoria=nombre_Categoria)
    context={
        'cat':cat,
        
        }
    return render(Request,"categoria.html",context)

