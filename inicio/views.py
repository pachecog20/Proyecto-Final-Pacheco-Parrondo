

from inicio.models import Articulo
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

def menu(request):
    return render(request, "inicio/menu.html")

def sobre_mi(request):
    return render(request, 'inicio/sobre_mi.html')
    

class ListaArticulos(ListView):
    model = Articulo
    template_name = "inicio/CBV/lista_articulos.html"
    
class CrearArticulos(LoginRequiredMixin,CreateView):
    model = Articulo
    template_name = "inicio/CBV/crear_articulos.html"
    success_url = reverse_lazy("inicio:listar_articulos")
    fields = ["nombre", "color", "version", "marca", "imagen"]
    
class ModificarArticulos(LoginRequiredMixin,UpdateView):
    model = Articulo
    template_name = "inicio/CBV/modificar_articulos.html"
    success_url = reverse_lazy("inicio:listar_articulos")
    fields = ["nombre", "color", "version", "marca", "cantidad_requerida", "imagen"]
    
class EliminarArticulos(LoginRequiredMixin,DeleteView):
    model = Articulo
    template_name = "inicio/CBV/eliminar_articulos.html"
    success_url = reverse_lazy("inicio:listar_articulos")
    
class MostrarArticulo(DetailView):
    model = Articulo
    template_name = "inicio/CBV/mostrar_articulos.html"