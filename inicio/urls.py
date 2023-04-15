from django.urls import path
from inicio import views

# app_name = "inicio"

urlpatterns = [
    path('inicio/', views.inicio, name ='Inicio'),
    path("mostrar-fecha/", views.mostrar_fecha, name ="MostrarFecha"),
    path("estudiantes/", views.estudiantes, name ="Estudiantes"),
    path("Cursos/", views.cursos, name ="Cursos"),
    path("profesores/", views.profesores, name ="Profesores"),
]
