from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('add/', views.add, name='add'),
    path('add/addequipo/',views.addequipo,name='addequipo'), 
    path('add/addjugador/',views.addjugador,name='addjugador'),

]