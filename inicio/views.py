
from datetime import datetime
from django.http import HttpResponse
from django.template import Template,Context, loader 
from inicio.models import Curso
from django.shortcuts import render, redirect
from inicio.forms import CreacionCursoFormulario


def menu(request):
    return render(request, "inicio/menu.html")


    
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
      

#def cursos(request):
   # if request.method == "POST":
    #    curso = Curso(nombre=request.POST['nombre'], camada= request.POST['camada'])
     #   curso.save()
    
    #return render(request, "inicio/cursos_v2.html")   
    
#v3
def cursos(request):
    if request.method == "POST":
        formulario = CreacionCursoFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            curso = Curso(nombre=datos_correctos['nombre'], camada= datos_correctos['camada'])
            curso.save()
            
            return redirect("inicio:listar_cursos")
    
    formulario = CreacionCursoFormulario()
    return render(request, "inicio/cursos_v3.html", {"formulario": formulario})       


def lista_cursos(request):
    return render(request, "inicio/lista_cursos.html", )     


def profesores(request):
    
    datos = {"nombre": "pepe"}
    
    # template = loader.get_template(r"prueba_render.html")
        
    # template_renderizado = template.render(datos)
        
    # return HttpResponse(template_renderizado)

    return render(request, r"inicio/profesores.html", datos)