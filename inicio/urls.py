from django.urls import path
from inicio import views

app_name = "inicio"

urlpatterns = [
    path('', views.mi_vista),
    path("mostrar-fecha/", views.mostrar_fecha),
    path("prueba-template/", views.prueba_template),
    path("crear-curso/", views.crear_curso),
    path("prueba-render/", views.prueba_render),
]
