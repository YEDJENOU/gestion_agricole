

# Create your models here.
from django.db import models
from producteurs.models import Producteur

class Stock(models.Model):
    producteur = models.ForeignKey(Producteur, on_delete=models.CASCADE)
    quantite = models.FloatField()
    type_stock = models.CharField(max_length=100)
    date_entree = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.producteur.nom} - {self.type_stock}"
