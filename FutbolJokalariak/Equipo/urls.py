from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('add/', views.add, name='add'),
    path('add/addequipo/',views.addequipo,name='addequipo'), 
    path('add/addjugador/',views.addjugador,name='addjugador'),
     path('add/addfichaje/',views.addfichaje,name='addfichaje'),
    #path('ezabatu/', views.deleteequipo, name='deleteequipo'),
    path ('eliminarequipo/<int:id>/', views.deleteequipo, name='deleteequipo'),
    path ('eliminarjugador/<int:id>/', views.deletejugador, name='deletejugador'),   
    path ('eliminarfichaje/<int:id>/', views.deletefichaje, name='deletefichaje'),
    path ('updateequipo/<int:id>/', views.updateequipo, name='updateequipo'),
    path ('editarequipo/<int:id>/', views.editarequipo, name='editarequipo'),

]