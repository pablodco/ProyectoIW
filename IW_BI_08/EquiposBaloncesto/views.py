from django.shortcuts import render
from .models import *
from django.http import *
from django.template import *
# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import categoria, equipo

def inicio(request):
    categorias = categoria.objects.order_by('nombreCategoria')
    categorias_con_equipos = []  # Lista para almacenar las categorías con sus respectivos equipos

    for categoria_obj in categorias:
        equipos_por_categoria = equipo.objects.filter(categoria=categoria_obj)
        categorias_con_equipos.append({
            'categoria': categoria_obj,
            'equipos': equipos_por_categoria
        })

    context = {
        'categorias_con_equipos': categorias_con_equipos
    }
    return render(request, "inicio.html", context)


def vistacategoria(Request,nombre_Categoria):
    cat=categoria.objects.get( nombreCategoria = nombre_Categoria)
    context={
        'cat':cat,
        }
    return render(Request,"categoria.html",context)

def vistaJugadores(Request,nombre_Categoria,nombre_Equipo):
    equipo1=equipo.objects.get(nombreEquipo=nombre_Equipo)
    context = {
        'equipo': equipo1
    }
    return render(Request,'equipo.html',context)

def vistaEquipoInfo(Request, nombre_Categoria, nombre_Equipo):
    equipo1 = equipo.objects.get(nombreEquipo = nombre_Equipo)
    context={
        'equipo': equipo1,
    }
    return render(Request,'equipoInfo.html',context)

def vistaNoticias(Request):
    categorias= categoria.objects.order_by('nombreCategoria')
    context = { 
        'categorias': categorias,
        }
    return render(Request,"noticia.html",context)

def inicio(Request):
    categorias= categoria.objects.order_by('nombreCategoria')
    context = { 
        'categorias': categorias,
        }
    return render(Request,"prueba.html",context)

def vistacategoria(Request,nombre_Categoria):
    cat=categoria.objects.get( nombreCategoria = nombre_Categoria)
    context={
        'cat':cat,
        }
    return render(Request,"categoria.html",context)

def vistaJugadores(Request,nombre_Categoria,nombre_Equipo):
    equipo1=equipo.objects.get(nombreEquipo=nombre_Equipo)
    context = {
        'equipo': equipo1
    }
    return render(Request,'equipo.html',context)

def vistaEquipoInfo(Request, nombre_Categoria, nombre_Equipo):
    equipo1 = equipo.objects.get(nombreEquipo = nombre_Equipo)
    context={
        'equipo': equipo1,
    }
    return render(Request,'equipoInfo.html',context)

def contacto(Request):
    return render(Request,'contacto.html')
class listaEquipos(ListView):
    model= equipo
    template_name="listaEquipos.html"
    context_object_name= 'equipo'

class listaJugadores(ListView):
    model= jugador
    template_name='jugadores.html'
    context_object_name= 'jugador'


class jugadorInfo(DetailView):
    model= jugador
    template_name='infoJugador.html'
    context_object_name= 'jugador'

class EquipoInfo(DetailView):
    model= equipo
    template_name='equipo.html'
    context_object_name= 'equipo'


class CategoriaInfo(DetailView):
    model= categoria
    template_name='categoria.html'
    context_object_name= 'cat'

class listaCategorias(ListView):
    model= categoria
    template_name='inicio.html'
    context_object_name= 'categorias'