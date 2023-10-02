from django.contrib import admin
from.models import Equipo
from.models import Jugador
from.models import Fichaje
# Register your models here.
#class PostAdmin(admin.ModelAdmin):
 #   list_display = ['nombre','ciudad','presidente','cuandocreado']

admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Fichaje)

