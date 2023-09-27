from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Equipo
from .models import Jugador
# Create your views here.
def index (request):
    equipos = Equipo.objects.all
    jugadores = Jugador.objects.all
    return render(request, 'index.html', {'equipo':equipos, 'jugador':jugadores})



def add(request):
    return render(request,'add.html')

def addequipo(request):
    nombre = request.POST["nombre"]
    ciudad = request.POST["ciudad"]
    presidente = request.POST["presidente"]
    equiponuevo = Equipo(nombre=nombre, ciudad=ciudad,presidente=presidente,cuandocreado="")
    equiponuevo.save()

    return HttpResponseRedirect(reverse('index'))

def addjugador(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    dorsal = request.POST["dorsal"]
    jugadornuevo = Jugador(nombre=nombre, apellido=apellido,dorsal=dorsal)
    jugadornuevo.save()

    return HttpResponseRedirect(reverse('index'))