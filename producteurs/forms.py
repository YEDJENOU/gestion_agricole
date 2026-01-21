from django import forms
from .models import Producteur, Arrondissement, Commune
from django.contrib.auth.models import User

class ProducteurForm(forms.ModelForm):
    class Meta:
        model = Producteur
        fields = ['user', 'nom', 'telephone', 'arrondissement', 'superficie']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'arrondissement': forms.Select(attrs={'class': 'form-control'}),
            'superficie': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ArrondissementForm(forms.ModelForm):
    class Meta:
        model = Arrondissement
        fields = ['nom', 'commune']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'commune': forms.Select(attrs={'class': 'form-control'}),
        }

class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
        }
