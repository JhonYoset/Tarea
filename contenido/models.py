from django.db import models

class Contenido(models.Model):
    nombre = models.CharField(max_length=255)
    autor = models.TextField()
    texto = models.TextField()