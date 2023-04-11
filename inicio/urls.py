from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.mi_vista),
    path("mi-primer-template/", views.mi_primer_template),
    path("mostrar-fecha/", views.mostrar_fecha),
    path("prueba-template/", views.prueba_template),
    path("crear-curso/", views.crear_curso),
]
