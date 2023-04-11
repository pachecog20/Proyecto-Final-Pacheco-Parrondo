from django.http import HttpResponse
from django.template import Template,Context 


def mi_vista(request):
    return HttpResponse("<h1>Que se destangue,terre terre terremoto pa tu cola</h1>")

def mi_primer_template(request):
    
    archivo = open(r"C:\Users\RAMIP\Desktop\proyecto3\proyecto-django\templates\mi_primer_template.html", "r")
    
    template = Template(archivo.read())
    
    archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)
    