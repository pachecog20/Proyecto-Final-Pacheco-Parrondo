
from datetime import datetime
from django.http import HttpResponse
from django.template import Template,Context, loader 
from inicio.models import Articulo
from django.shortcuts import render, redirect
from inicio.forms import CreacionArticuloFormulario, BuscarArticulo


def menu(request):
    return render(request, "inicio/menu.html")



def articulos(request):
    if request.method == "POST":
        formulario = CreacionArticuloFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            curso = Articulo(nombre=datos_correctos['nombre'], color= datos_correctos['color'],version= datos_correctos['version'], marca= datos_correctos['marca'])
            curso.save()
            
            return redirect("inicio:Articulos")
    
    formulario = CreacionArticuloFormulario()
    return render(request, "inicio/articulos.html", {"formulario": formulario})    
   


def lista_articulos(request):
    nombre_a_buscar= request.GET.get("nombre", None)
    
    if nombre_a_buscar:
        articulos=Articulo.objects.filter(nombre__icontains=nombre_a_buscar)
    else: 
        articulos = Articulo.objects.all()
    formulario_busqueda = BuscarArticulo()
    return render(request, "inicio/lista_articulos.html", {"articulos":articulos, "formulario":formulario_busqueda} )     

