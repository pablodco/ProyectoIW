from . import views
from django.urls import *
urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('<str:nombre_Categoria>/',views.vistacategoria,name='categoria'),
    #path('<str:nombreCategoria>/<str:nombreEquipo>',views, name='equipo'),*/
    path('<str:nombreEquipo>/<str:nombreJugador>', views.jugador, name='jugador'),
]