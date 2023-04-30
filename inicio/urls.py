from django.urls import path
from inicio import views

app_name = "inicio"

urlpatterns = [
    path('', views.menu, name ='inicio'),
    
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    
    path("Articulos/<int:pk>/", views.MostrarArticulo.as_view(), name ="mostrar_articulos"),
     
    path("Articulos/Lista/", views.ListaArticulos.as_view(), name ="listar_articulos"),
    path("Articulos/", views.CrearArticulos.as_view(), name ="Articulos"),
    path("Articulos/<int:pk>/Modificar/", views.ModificarArticulos.as_view() , name ="modificar_articulos"), 
    path("Articulos/<int:pk>/Eliminar/", views.EliminarArticulos.as_view() , name ="eliminar_articulos"),
]
