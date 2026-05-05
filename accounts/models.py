from django.db import models

class Abonne(models.Model):
    contact = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)
