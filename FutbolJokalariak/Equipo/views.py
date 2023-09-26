from django.shortcuts import render

# Create your views here.
from .models import Equipo

# Create your views here.
def index (request):
    equipos = Equipo.objects.all
    return render(request, 'index.html', {'equipo':equipos})