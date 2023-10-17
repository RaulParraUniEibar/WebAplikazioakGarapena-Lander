from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gehitu/',views.gehitu,name='gehitu'),
    path('gehitu/gehituerregistroa/',views.gehituerregistroa,name='gehituerregistroa'),
    path('ezabatu/<matrikula>',views.ezabatu,name='ezabatu'),
    path('eguneratu/<matrikula>',views.eguneratu,name='eguneratu'),
    path('eguneratu/eguneratuerregistroa/<matrikula>', views.eguneratuerregistroa, name='eguneratuerregistroa'),
    path('bezeroak/',views.bezeroak,name='bezeroak'),
    path('bezeroak/gehitubezeroa/', views.gehitubezeroa,name='gehitubezeroa'),
    path('bezeroak/gehitubezeroa/gehituerregistrobezeroa/',views.gehituerregistrobezeroa,name='gehituerregistrobezeroa'),
    path('bezeroak/ezabatubezero/<dni>',views.ezabatubezero,name='ezabatubezero'),
    path('bezeroak/eguneratubezero/<dni>',views.eguneratubezero,name='eguneratubezero'),
    path('bezeroak/eguneratubezero/eguneratuerregistroaBezeroa/<dni>',views.eguneratuerregistroaBezeroa,name='eguneratuerregistroaBezeroa'),
    path('alokairuak/',views.alokairuak,name='alokairuak'),
    path('alokairuak/gehitualokairua/',views.gehitualokairua,name='gehitualokairua'),
    path('alokairuak/gehitualokairua/gehituerregistroalokairua/',views.gehituerregistroalokairua,name='gehituerregistroalokairua'),
]