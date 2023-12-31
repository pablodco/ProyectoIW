from django.db import models

# Create your models here.
class jugador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacionalidad = models.URLField(null=True)
    posicion = models.CharField(max_length=30)
    puntosPorPartido= models.FloatField()
    asistenciasPorPartido= models.FloatField()
    rebotesPorPartido= models.FloatField()
    taponesPorPartido= models.FloatField()
    robosPorPartido= models.FloatField()
    partidosJugados= models.IntegerField()
    añoDraft= models.IntegerField()
    dorsal= models.IntegerField()
    equipo= models.ForeignKey('equipo',on_delete=models.CASCADE, related_name='jugadores')
    imagen=models.URLField(null=True)

class equipo(models.Model):
    nombreEquipo = models.CharField(max_length=40, unique=True)
    ciudad = models.CharField(max_length=40)
    nombrePropietario= models.CharField(max_length=40)
    categoria= models.ForeignKey('categoria',on_delete=models.CASCADE, related_name='equipos')
    logo= models.URLField(null=True)

class categoria(models.Model):
    nombreCategoria = models.CharField(max_length=40,unique=True)
    descripcion = models.TextField()
    premio= models.CharField(max_length=30)
    logo= models.URLField(null=True)

class noticia(models.Model):
    titularNoticia = models.CharField(max_length=20, unique=True)
    descNoticia = models.CharField(max_length=100, unique=True)
    textoImg = models.CharField(max_length=40, unique=True)
    categoria= models.ForeignKey('categoria',on_delete=models.CASCADE, related_name='noticias')
    imgNoticia = models.URLField(null=True)