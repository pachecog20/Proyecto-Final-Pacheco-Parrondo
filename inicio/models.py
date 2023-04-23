from django.db import models

# Create your models here.

class Articulo(models.Model):
    nombre = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    version = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    cantidad_requerida = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{self.nombre}, {self.color}, {self.version}, {self.marca}"
    
    

