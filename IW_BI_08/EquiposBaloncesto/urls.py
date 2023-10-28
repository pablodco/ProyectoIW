from . import views
from django.urls import *
urlpatterns=[
    path('<str:nombreJugador>', views.inicio, name='inicio')
]