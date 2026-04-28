from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
from django.db import models

class Abonne(models.Model):
    nom = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nom or "Sans nom"
