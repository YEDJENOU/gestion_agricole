

from django.urls import path
from . import views

urlpatterns = [
     path('', views.dashboard, name='dashboard'),
        path('liste', views.liste_producteurs, name='liste_producteurs'),
    path('ajouter/', views.ajouter_producteur, name='ajouter_producteur'),
]
