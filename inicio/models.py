from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Articulo(models.Model):
    nombre = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    version = RichTextField()
    marca = models.CharField(max_length=20)
    cantidad_requerida = models.IntegerField(null=True)
   
    
    def __str__(self):
        return f"{self.nombre}, {self.marca}"
    
    

