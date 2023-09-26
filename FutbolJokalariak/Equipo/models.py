from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=300)
    presidente = models.CharField(max_length=100)
    cuandocreado = models.DateTimeField(auto_now_add=True)

    def __unicode__ (self):
        return self.nombre
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dorsal = models.IntegerField()

    def __unicode__ (self):
        return self.nombre
    