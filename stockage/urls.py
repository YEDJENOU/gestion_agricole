from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_stock, name='liste_stock'),
    path('ajouter/', views.ajouter_stock, name='ajouter_stock'),
]
