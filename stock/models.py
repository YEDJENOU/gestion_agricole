from django.db import models

# Create your models here.
from django.db import models
from recoltes.models import Culture

class Entrepot(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.CharField(max_length=150)

    def __str__(self):
        return self.nom


class Stock(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    entrepot = models.ForeignKey(Entrepot, on_delete=models.CASCADE)
    quantite = models.FloatField()
    seuil_alerte = models.FloatField(default=100)

    def alerte_stock_bas(self):
        return self.quantite < self.seuil_alerte
