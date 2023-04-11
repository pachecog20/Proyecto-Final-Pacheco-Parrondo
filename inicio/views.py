
from datetime import datetime
from django.http import HttpResponse
from django.template import Template,Context, loader 
from inicio.models import Curso



def mi_vista(request):
    return HttpResponse("<h1>Que se destangue,terre terre terremoto pa tu cola</h1>")

def mi_primer_template(request):
    
    archivo = open(r"C:\Users\RAMIP\Desktop\proyecto3\proyecto-django\templates\mi_primer_template.html", "r")
    
    template = Template(archivo.read())
    
    archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)
    
def mostrar_fecha(request):
         
        dt = datetime.now()
    
        dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
    
        template = loader.get_template(r"mostrar_fecha.html")
        
        template_renderizado = template.render({"fecha": dt_formateado})
        
        return HttpResponse(template_renderizado)
    
def prueba_template(request):
        
        datos ={
            "nombre": "Geronimo",
            "apellido": "Pacheco",
            "edad": 20,    
        }
         
        template = loader.get_template(r"prueba_template.html")
        
        template_renderizado = template.render(datos)
        
        return HttpResponse(template_renderizado)
    
    
def crear_curso(request):
    
    curso = Curso(nombre="CoderHouse",camada= 333)
    print(curso.nombre)
    print(curso.camada)
    curso.save()
    
    datos = {"curso": curso} 

    template = loader.get_template(r"crear_curso.html")
        
    template_renderizado = template.render(datos)
        
    return HttpResponse(template_renderizado)
    