from django.urls import path
from inicio import views

app_name = "inicio"

urlpatterns = [
    path('', views.menu, name ='Menu'),
    path("Articulos/", views.articulos, name ="Articulos"),
    path("Lista-Articulos/", views.lista_articulos, name ="listar_articulos"),
    
]
