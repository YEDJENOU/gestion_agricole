from django.contrib.auth.models import User

from django.db import models

# Create your models here.
from django.db import models

class Commune(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Arrondissement(models.Model):
    nom = models.CharField(max_length=100)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} ({self.commune.nom})"


class Producteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    nom = models.CharField(max_length=150)
    telephone = models.CharField(max_length=20)
    arrondissement = models.ForeignKey(Arrondissement, on_delete=models.CASCADE)
    superficie = models.FloatField()

    def __str__(self):
        return self.nom
