from django import forms

class CreacionArticuloFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    version = forms.IntegerField()
    marca = forms.CharField(max_length=20)
    
class BuscarArticulo(forms.Form):
    nombre = forms.CharField(max_length=20)