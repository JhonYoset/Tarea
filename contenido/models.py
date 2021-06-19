from django.db import models

# Create your models here.
class Contenido(models.Model):
    nombre = models.CharField(max_length=255)
    autor = models.CharField(max_length=200)
    texto = models.TextField()
