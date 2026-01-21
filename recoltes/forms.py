from django import forms
from .models import Recolte, Culture
from producteurs.models import Producteur

class RecolteForm(forms.ModelForm):
    class Meta:
        model = Recolte
        fields = ['producteur', 'culture', 'quantite',]
        widgets = {
            'producteur': forms.Select(attrs={'class': 'form-control'}),
            'culture': forms.Select(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CultureForm(forms.ModelForm):
    class Meta:
        model = Culture
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
        }
