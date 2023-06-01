from django import forms

class CreacionArticuloFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    version = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    cantidad_requerida = forms.IntegerField(required=False)
    imagen= forms.ImageField(required=False)
    
class ModificarArticuloFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    version = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)   
    cantidad_requerida = forms.IntegerField(required=False)
    imagen= forms.ImageField(required=False)
    
class BuscarArticulo(forms.Form):
    nombre = forms.CharField(max_length=20)