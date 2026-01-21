

# Create your models here.
from django.db import models
from producteurs.models import Producteur

class Culture(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Recolte(models.Model):
    producteur = models.ForeignKey(Producteur, on_delete=models.CASCADE)
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    quantite = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.producteur.nom} - {self.culture.nom}"
