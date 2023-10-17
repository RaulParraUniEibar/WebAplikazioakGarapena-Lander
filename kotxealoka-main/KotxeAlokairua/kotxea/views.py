from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from kotxea.models import Alokairua, Bezeroa, Kotxea

# Create your views here.
def index(request):
    kotxeak = Kotxea.objects.all
    return render(request, 'index.html',{'kotxeak':kotxeak})

def gehitu(request):
    return render(request, 'gehitu.html')

def gehituerregistroa(request):
    matrikula = request.POST['matrikula']
    marka = request.POST['marka']
    prezioa = request.POST['prezioa']

    kotxea= Kotxea(matrikula=matrikula, marka=marka, prezioa=prezioa)
    kotxea.save()
    return HttpResponseRedirect(reverse('index'))

def ezabatu(request, matrikula):
    kotxea = Kotxea.objects.get(matrikula=matrikula)
    kotxea.delete()
    return HttpResponseRedirect(reverse('index'))

def eguneratu(request, matrikula):
    kotxea = Kotxea.objects.get(matrikula=matrikula)
    return render(request, 'eguneratu.html', {'kotxea': kotxea})

def eguneratuerregistroa(request, matrikula):
    matrikula = request.POST['matrikula']
    marka = request.POST['marka']
    prezioa = request.POST['prezioa']
    kotxea = Kotxea.objects.get(matrikula=matrikula)
    kotxea.matrikula = matrikula
    kotxea.marka = marka
    kotxea.prezioa = prezioa
    kotxea.save()
    return HttpResponseRedirect(reverse('index'))

def bezeroak(request):
    bezeroak = Bezeroa.objects.all
    return render(request, 'bezeroak.html',{'bezeroak':bezeroak})

def gehitubezeroa(request):
    return render(request, 'bezeroak_gehitu.html')

def gehituerregistrobezeroa(request):
    dni = request.POST['dni']
    izena = request.POST['izena']
    abizena = request.POST['abizena']
    adina = request.POST['adina']

    bezeroa= Bezeroa(dni=dni, izena=izena, abizena=abizena, adina=adina)
    bezeroa.save()
    return HttpResponseRedirect(reverse('index'))


def ezabatubezero(request, dni):
    bezeroa = Bezeroa.objects.get(dni=dni)
    bezeroa.delete()
    return HttpResponseRedirect(reverse('bezeroak'))

def eguneratubezero(request, dni):
    bezeroa = Bezeroa.objects.get(dni=dni)
    return render(request, 'bezeroak_eguneratu.html', {'bezeroa': bezeroa})

def eguneratuerregistroaBezeroa(request, dni):
    dni = request.POST['dni']
    izena = request.POST['izena']
    abizena = request.POST['abizena']
    adina = request.POST['adina']
    bezeroa = Bezeroa.objects.get(dni=dni)
    bezeroa.matrikula = dni
    bezeroa.marka = izena
    bezeroa.prezioa = abizena
    bezeroa.adina = adina
    bezeroa.save()
    return HttpResponseRedirect(reverse('index'))

def alokairuak(request):
    alokairuak = Alokairua.objects.all
    return render(request, 'alokairuak.html',{'alokairuak':alokairuak})

def gehitualokairua(request):
    kotxeak = Kotxea.objects.all
    bezeroak = Bezeroa.objects.all
    return render(request, 'alokairuak_gehitu.html', {'kotxeak':kotxeak, 'bezeroak':bezeroak})

def gehituerregistroalokairua(request):
    bezeroa = request.POST['bezero_dni']
    bezeroaOndo= Bezeroa.objects.get(izena=bezeroa)
    kotxea = request.POST['kotxe_matrikula']
    kotxeaOndo= Kotxea.objects.get(marka=kotxea)
    hasiera_data = request.POST['alokairu_data_hasi']
    bukaera_data = request.POST['alokairu_data_bukatu']

    alokairua= Alokairua(bezero_dni=bezeroaOndo, kotxe_matrikula=kotxeaOndo, alokairu_data_hasi=hasiera_data, alokairu_data_bukatu=bukaera_data)
    alokairua.save()
    return HttpResponseRedirect(reverse('index'))