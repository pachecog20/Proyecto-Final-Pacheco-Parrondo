from django import forms

class CreacionCursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    