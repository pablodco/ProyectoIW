from django.contrib import admin
from .models import *
from . import models
# Register your models here.
admin.site.register(jugador)
admin.site.register(equipo)
admin.site.register(categoria)
