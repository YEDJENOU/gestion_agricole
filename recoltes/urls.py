from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_recoltes, name='liste_recoltes'),
    path('ajouter/', views.ajouter_recolte, name='ajouter_recolte'),
    path('modifier/<int:id>/', views.modifier_recolte, name='modifier_recolte'),
    path('supprimer/<int:id>/', views.supprimer_recolte, name='supprimer_recolte'),
]
