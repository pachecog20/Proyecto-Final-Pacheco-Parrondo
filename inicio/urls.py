from django.urls import path
from inicio import views

app_name = "inicio"

urlpatterns = [
    path('', views.menu, name ='Menu'),
    
    
    
   #path("Articulos/", views.articulos, name ="Articulos"),
   # path("Articulos/Lista/", views.lista_articulos, name ="listar_articulos"),
   # path("Articulos/<int:id_articulo>/Eliminar/", views.eliminar_articulo, name ="eliminar_articulos"),  
    #path("Articulos/<int:id_articulo>/Modificar/", views.modificar_articulo, name ="modificar_articulos"),  
    path("Articulos/<int:pk>/", views.MostrarArticulo.as_view(), name ="mostrar_articulos"), 
    path("Articulos/Lista/", views.ListaArticulos.as_view(), name ="listar_articulos"),
    path("Articulos/", views.CrearArticulos.as_view(), name ="Articulos"),
    path("Articulos/<int:pk>/Modificar/", views.ModificarArticulos.as_view() , name ="modificar_articulos"), 
    path("Articulos/<int:pk>/Eliminar/", views.EliminarArticulos.as_view() , name ="eliminar_articulos"),
]
