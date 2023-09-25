from django.contrib import admin
from.models import Equipo
from.models import Jugador
# Register your models here.
#class PostAdmin(admin.ModelAdmin):
 #   list_display = ['nombre','ciudad','presidente','cuandocreado']

admin.site.register(Equipo)
admin.site.register(Jugador)

