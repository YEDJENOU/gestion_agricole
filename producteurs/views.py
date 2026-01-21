from django.shortcuts import render, redirect
from .forms import ProducteurForm
from .models import Producteur


def dashboard(request):
    return render(request, 'producteurs/dashboard.html')

# Liste des producteurs
def liste_producteurs(request):
    producteurs = Producteur.objects.all()
    return render(request, 'producteurs/liste_producteurs.html', {'producteurs': producteurs})

# Ajouter un producteur
def ajouter_producteur(request):
    if request.method == 'POST':
        form = ProducteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_producteurs')
    else:
        form = ProducteurForm()
    return render(request, 'producteurs/ajouter_producteur.html', {'form': form})
