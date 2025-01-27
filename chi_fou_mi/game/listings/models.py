from django.db import models

class Sign(models.Model):
    nom = models.fields.CharField(max_length=20, blank=False)
    prenom = models.fields.CharField(max_length=20, blank=False)
    email = models.fields.EmailField(max_length=50, blank=False, unique=True)
    password = models.fields.CharField(max_length=20, blank=False)
    confirmation = models.fields.CharField(max_length=20, blank=False)
