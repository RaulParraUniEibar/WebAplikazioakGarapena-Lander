from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Equipo
from .models import Jugador
from .models import Fichaje
# Create your views here.
def index (request):
    equipos = Equipo.objects.all
    jugadores = Jugador.objects.all
    fichaje = Fichaje.objects.all
    return render(request, 'index.html', {'equipo':equipos, 'jugador':jugadores,'fichaje':fichaje})



def add(request):
    equipos = Equipo.objects.all
    jugadores = Jugador.objects.all
    return render(request,'add.html', {'equipo':equipos, 'jugador':jugadores})

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

def addfichaje(request):
    jugid = request.POST["nombreju"]
    equipid = request.POST["nombreeq"]
    temporada = request.POST["temporada"]

    jug = Jugador.objects.get(id = jugid)
    eq = Equipo.objects.get(id = equipid)

    fichajenuevo = Fichaje(temporada=temporada, equipofichaje= eq, jugadorfichaje=jug)
    fichajenuevo.save()

    return HttpResponseRedirect(reverse('index'))

def deleteequipo(request, id):
    equipoeliminar = Equipo.objects.get(id = id) #pasar el equipo
    Equipo.delete(equipoeliminar) #ezabatu

    return HttpResponseRedirect(reverse(index))

def deletejugador(request, id):
    jugadoreliminar = Jugador.objects.get(id = id) #pasar el equipo
    Jugador.delete(jugadoreliminar) #ezabatu

    return HttpResponseRedirect(reverse(index))

def deletefichaje(request, id):
    fichajeeliminar = Fichaje.objects.get(id = id) #pasar el equipo
    Jugador.delete(fichajeeliminar) #ezabatu

    return HttpResponseRedirect(reverse(index))

def updateequipo(request, id):
    equipoUpdate = Equipo.objects.get(id = id)
    return render(request,'update.html', {'equip':equipoUpdate})

def editarequipo(request, id):

    equipoeditar = Equipo.objects.get(id = id) #pasar el id del equipo

    nombre = request.POST["nombre"]
    ciudad = request.POST["ciudad"]
    presidente = request.POST["presidente"]

    equipoeditar.nombre = nombre
    equipoeditar.ciudad = ciudad
    equipoeditar.presidente = presidente
    equipoeditar.save()
       
    return HttpResponseRedirect(reverse(index))
