from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

def algoritmos(request):
    template = loader.get_template('principal.html')
    saludo = "Bienvenido a mi presentación"
    context = {
        'saludo' : saludo
    }
    return HttpResponse(template.render(context,request))