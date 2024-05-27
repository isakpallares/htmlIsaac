from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

def principal(request):
    template = loader.get_template('principal.html')
    inicio = "Bienvenido a mi Portafolio"
    desc =    "Aquí podrás saber un poco de mi, lo que hago y el cómo ayudaré en su empresa."
    context = {
        'inicio' : inicio,
        'descripcion' : desc
    }
    return HttpResponse(template.render(context,request))
    
def principalEn(request):
    template = loader.get_template('principalEn.html')
    inicio = "Welcome to my portfolio"
    desc =    "Here you will know more about me, what i do and how i will help in your company"
    context = {
        'inicio' : inicio,
        'descripcion' : desc
    }
    return HttpResponse(template.render(context,request))
    
def portfolio(request):
   return render(request,'portfolio.html')
   
def portfolioEn(request):
    return render(request,'portfolioEn.html')

def contacto(request):
    return render(request,'contacto.html')
    
def contactoEn(request):
    return render(request,'contactoEn.html')