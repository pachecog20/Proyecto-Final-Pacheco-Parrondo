from django.db import models

# Create your models here.

class Articulo(models.Model):
    nombre = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    version = models.IntegerField()
    marca = models.CharField(max_length=20)
    
