from django.db import models

# Create your models here.
class jugador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=15)
    puntosPorPartido= models.FloatField()
    asistenciasPorPartido= models.FloatField()
    rebotesPorPartido= models.FloatField()
    taponesPorPartido= models.FloatField()
    robosPorPartido= models.FloatField()
    partidosJugados= models.IntegerField()
    añoDraft= models.IntegerField()
    dorsal= models.IntegerField()
    equipo= models.ForeignKey('equipo',on_delete=models.CASCADE)

class equipo(models.Model):
    nombreEquipo = models.CharField(max_length=40, unique=True)
    ciudad = models.CharField(max_length=40)
    nombrePropietario= models.CharField(max_length=40)
    categoria= models.ForeignKey('categoria',on_delete=models.CASCADE, related_name='equipos')

class categoria(models.Model):
    nombreCategoria = models.CharField(max_length=40,unique=True)
    descripcion = models.TextField()
    premio= models.CharField(max_length=30)
    