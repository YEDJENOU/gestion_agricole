from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Recolte
from producteurs.models import Producteur

def mes_recoltes(request):
    producteur = Producteur.objects.get(user=request.user)
    recoltes = Recolte.objects.filter(producteur=producteur)
    return render(request, "recoltes/mes_recoltes.html", {"recoltes": recoltes})
