from . import views
from django.urls import *
urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('<str:nombre_Categoria>/',views.vistacategoria,name='categoria'),
    path('<str:nombre_Categoria>/<str:nombre_Equipo>/Informacion', views.vistaEquipoInfo, name='Equipoinfo'),
    #path('<str:nombreCategoria>/<str:nombreEquipo>',views, name='equipo'),*/
    path('<str:nombre_Categoria>/<str:nombre_Equipo>', views.vistaJugadores, name='equipo'),
    path('noticias/', views.vistaNoticias, name='noticia'),
]