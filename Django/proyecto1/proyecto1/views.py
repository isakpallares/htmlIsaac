from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime
import math
from django.shortcuts import render
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
def saludo_plantilla_loader(request):
    p1 = Persona("Juan Fernando", "Galan",28)
    fecha_actual = datetime.datetime.now()
    
    materias = ["Algoritmos", "Base de Datos", "Java","Python"]
    # materias = []
    doc_externo = loader.get_template('miplantilla.html')
    contexto = {
    "nombre_profesor":p1.nombre,
    "edad" : p1.edad,
    "fecha" : fecha_actual,
    "materias" : materias,
    }
    documento = doc_externo.render(contexto)
    return HttpResponse(documento)
    
    
def saludo_plantilla_clase(request):
    p1 = Persona("Juan Fernando", "Galan",28)
    fecha_actual = datetime.datetime.now()
    
    materias = ["Algoritmos", "Base de Datos", "Java","Python"]
    materias = []
    aulas = ["Robles","Blanco","Turpial","Bolivar"]
    doc_externo = open("D:/ADSO-8/desarrolloWeb/Django/proyecto1/proyecto1/plantilla/miplantilla.html",)
    nombre ="Omar"
    plantilla = Template(doc_externo.read())  
    doc_externo.close()
    contexto = Context({
    "nombre_profesor":p1.nombre,
    "edad" : p1.edad,
    "fecha" : fecha_actual,
    "materias" : materias,
    "aulas" : aulas
    })
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
    
def plantilla_datos(request):
    doc_externo = open("D:/ADSO-8/desarrolloWeb/Django/proyecto1/proyecto1/plantilla/plantilladylan.html",)
    
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def saludo(request):
    documento="<html><body><h1> Primera página de Django </h1></body></html>"
    return HttpResponse(documento)
def algoritmos(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "algoritmos.html",{"obtener_fecha":fecha_actual})

def scrum(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "scrum.html",{"obtener_fecha":fecha_actual})

def despedida(request):
    return HttpResponse("Hasta Luego Adso 8 Django")
#Vista para mostrar fecha y hora
def dame_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento=f"<html><body><h2>Fecha y hora actual: </h2><p>{fecha_actual}</p></body></html>"
    return HttpResponse(documento)
#Saluda con el nombre pasado
def saludopersonal(request,numero):
    total=numero+10
    documento=f"<html><body><h2>Hola {total} </h2></body></html>"
    return HttpResponse(documento)
#Calcular edad futura d euna persona de 18 años a partir del año 2024
def calcula_edad(request,anio):
    edad_actual=18
    periodo=anio-2024
    edad_futura=edad_actual+periodo
    documento=f"<html><body><h2>En el año {anio} tendras {edad_futura} </h2></body></html>"
    return HttpResponse(documento)
def calcula_edad_futura(request,edad_actual,anio):
    periodo=anio-2024
    edad_futura=edad_actual+periodo
    documento=f"<html><body><h2>En el año {anio} tendras {edad_futura} </h2></body></html>"
    return HttpResponse(documento)

def saludo_personalizado(request,nombre):
    doc_externo = open("D:\ADSO-8\desarrolloWeb\Django\proyecto1\proyecto1\plantilla\plantilla_uno.html",)
    plantilla = Template(doc_externo.read())  
    doc_externo.close()
    contexto = Context({"nombre":nombre})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
    
def perfil_usuario(request,usuario,seccion):
    doc_externo = open("D:\ADSO-8\desarrolloWeb\Django\proyecto1\proyecto1\plantilla\plantilla_dos.html",)
    plantilla = Template(doc_externo.read())  
    doc_externo.close()
    contexto = Context({"usuario":usuario,
                        "seccion":seccion})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)  
    
def calcular_hipotenusa(request,lado_a, lado_b):
    doc_externo = open("D:\ADSO-8\desarrolloWeb\Django\proyecto1\proyecto1\plantilla\plantilla_tres.html",)
    hipotenusa = math.sqrt(lado_a**2 + lado_b**2)
    plantilla = Template(doc_externo.read())  
    doc_externo.close()
    contexto = Context({"ladoa":lado_a,
                        "ladob":lado_b,
                        "hipotenusa":hipotenusa})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)  
    
def mayor_edad(request,edad):
    legal = "Es mayor de edad"
    if edad<18:
        legal  = "Es menor de edad"
    doc_externo = open("D:\ADSO-8\desarrolloWeb\Django\proyecto1\proyecto1\plantilla\plantilla_cuatro.html",)
    plantilla = Template(doc_externo.read())  
    doc_externo.close()
    contexto = Context({"edad":edad,"legal":legal})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def salario_empleado(request,empleado, horas, valor_hora,impuesto):
    doc_externo = open("D:\ADSO-8\desarrolloWeb\Django\proyecto1\proyecto1\plantilla\plantilla_cinco.html",)
    plantilla = Template(doc_externo.read())  
    doc_externo.close()
    salario_base = horas * valor_hora
    cantidad_descuento = salario_base * (impuesto/100)
    salario_descuento = salario_base - cantidad_descuento
    contexto = Context({"empleado":empleado,
        "horas" : horas,
        "valor_hora" : valor_hora,
        "impuesto" : impuesto,
        "salario_descuento" : salario_descuento
    })
    documento = plantilla.render(contexto)
    return HttpResponse(documento)