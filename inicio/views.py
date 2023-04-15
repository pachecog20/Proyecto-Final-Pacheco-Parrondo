
from datetime import datetime
from django.http import HttpResponse
from django.template import Template,Context, loader 
from inicio.models import Curso
from django.shortcuts import render



def inicio(request):
    return render(request, "inicio/inicio.html")


    
def mostrar_fecha(request):
         
        dt = datetime.now()
    
        dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
    
        template = loader.get_template(r"inicio/mostrar_fecha.html")
        
        template_renderizado = template.render({"fecha": dt_formateado})
        
        return HttpResponse(template_renderizado)
    
def estudiantes(request):
        
        datos ={
            "nombre": "Geronimo",
            "apellido": "Pacheco",
            "edad": 20,    
        }
         
        template = loader.get_template(r"inicio/estudiantes.html")
        
        template_renderizado = template.render(datos)
        
        return HttpResponse(template_renderizado)
    
    
def cursos(request):
    
    curso = Curso(nombre="CoderHouse",camada= 333)
    print(curso.nombre)
    print(curso.camada)
    curso.save()
    
    datos = {"curso": curso} 

    template = loader.get_template(r"inicio/cursos.html")
        
    template_renderizado = template.render(datos)
        
    return HttpResponse(template_renderizado)
    
    
def profesores(request):
    
    datos = {"nombre": "pepe"}
    
    # template = loader.get_template(r"prueba_render.html")
        
    # template_renderizado = template.render(datos)
        
    # return HttpResponse(template_renderizado)

    return render(request, r"inicio/profesores.html", datos)