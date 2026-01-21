from django.shortcuts import render, redirect, get_object_or_404
from .models import Recolte
from .forms import RecolteForm

def liste_recoltes(request):
    recoltes = Recolte.objects.all()
    return render(request, 'recoltes/recoltes.html', {'recoltes': recoltes})

def ajouter_recolte(request):
    form = RecolteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_recoltes')
    return render(request, 'recoltes/form_recolte.html', {'form': form})

def modifier_recolte(request, id):
    recolte = get_object_or_404(Recolte, id=id)
    form = RecolteForm(request.POST or None, instance=recolte)
    if form.is_valid():
        form.save()
        return redirect('liste_recoltes')
    return render(request, 'recoltes/form_recolte.html', {'form': form})

def supprimer_recolte(request, id):
    recolte = get_object_or_404(Recolte, id=id)
    recolte.delete()
    return redirect('liste_recoltes')
