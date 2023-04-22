from django.urls import path
from inicio import views

app_name = "inicio"

urlpatterns = [
    path('', views.menu, name ='Menu'),
    path("Articulos/", views.articulos, name ="Articulos"),
    path("Articulos/Lista/", views.lista_articulos, name ="listar_articulos"),
    path("Articulos/<int:id_articulo>/Eliminar/", views.eliminar_articulo, name ="eliminar_articulos"),  
    path("Articulos/<int:id_articulo>/Modificar/", views.modificar_articulo, name ="modificar_articulos"),  
    path("Articulos/<int:id_articulo>/", views.mostrar_articulo, name ="mostrar_articulos"), 
]
