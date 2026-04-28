from django.db import models

class Abonne(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom
class Abonne(models.Model):
    contact = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)
