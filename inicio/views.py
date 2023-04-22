
from datetime import datetime
from django.http import HttpResponse
from django.template import Template,Context, loader 
from inicio.models import Articulo
from django.shortcuts import render, redirect
from inicio.forms import CreacionArticuloFormulario, BuscarArticulo, ModificarArticuloFormulario


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

def eliminar_articulo(request, id_articulo):
    articulo_a_eliminar = Articulo.objects.get(id=id_articulo)
    articulo_a_eliminar.delete()
    return redirect("inicio:listar_articulos")

def mostrar_articulo(request, id_articulo):
    articulo_a_mostrar = Articulo.objects.get(id=id_articulo)
    return render(request, "inicio/mostrar_articulos.html", {"articulo_a_mostrar":articulo_a_mostrar} )  
    

def modificar_articulo(request, id_articulo):
    articulo_a_modificar = Articulo.objects.get(id=id_articulo)
    
    if request.method == "POST":
        formulario = ModificarArticuloFormulario(request.POST)
        if formulario.is_valid():
            data_limpia = formulario.cleaned_data
            articulo_a_modificar.nombre = data_limpia["nombre"]
            articulo_a_modificar.color = data_limpia["color"]
            articulo_a_modificar.version = data_limpia["version"]
            articulo_a_modificar.marca = data_limpia["marca"]
            articulo_a_modificar.save()
            return redirect("inicio:listar_articulos")
    
    formulario = ModificarArticuloFormulario(initial={"nombre":articulo_a_modificar.nombre,"color":articulo_a_modificar.color,"version":articulo_a_modificar.version,"marca":articulo_a_modificar.marca })
    return render(request, "inicio/modificar_articulos.html", {"formulario": formulario, "id_articulo" : id_articulo})

    