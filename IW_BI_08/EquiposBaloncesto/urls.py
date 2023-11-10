from . import views
from django.urls import *
urlpatterns=[
    path('', views.listaCategorias.as_view(), name='inicio'), 
    path('<str:nombre_Categoria>/<slug:pk>', views.EquipoInfo.as_view(), name='equipo'),
    #path('<str:nombre_Categoria>/<str:nombreEquipo>/<slug:pk>', views.jugadorInfo.as_view(), name='jugador'),
    #path('<slug:pk>', views.CategoriaInfo.as_view(), name='categoria'),
    path('<str:nombre_Categoria>/',views.vistacategoria,name='categoria'),
    path('<str:nombre_Categoria>/<str:nombre_Equipo>/Informacion', views.vistaEquipoInfo, name='Equipoinfo'),
    #path('<str:nombreCategoria>/<str:nombreEquipo>',views, name='equipo'),*/
    path('<str:nombre_Categoria>/<str:nombre_Equipo>', views.vistaJugadores, name='equipo'),
    path('noticias', views.vistaNoticias, name='noticia'),
    path('contacto', views.contacto ,name='contacto')
]