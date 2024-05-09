from django.http import HttpResponse
import datetime
import math
def saludo(request):
    documento="<html><body><h1> Primera página de Django </h1></body></html>"
    return HttpResponse(documento)


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
    documento=f"<html><body><h2>Bienvenido </h2><p>Bienvenido {nombre} a esta pagina!</p></body></html>"
    return HttpResponse(documento)
    
def perfil_usuario(request,usuario,seccion):
    documento=f"<html><body><h2>Bienvenido usuario</h2><p>Sr/a {usuario}, su seccion solicitada es: {seccion}</p></body></html>"
    return HttpResponse(documento)  
    
def calcular_hipotenusa(request,lado_a, lado_b):
    hipotenusa = math.sqrt(lado_a**2 + lado_b**2)
    documento=f"<html><body><h2>Bienvenido usuario</h2><p>La hipotenusa del triangulo con lado {lado_a} y {lado_b}, es: {hipotenusa}</p></body></html>"
    return HttpResponse(documento)  
    
def mayor_edad(request,edad):
    legal = "Es mayor de edad"
    if edad<18:
        legal  = "Es menor de edad"

    documento=f"<html><body><h2>Bienvenido usuario</h2><p>Tu edad es: {edad}, eres {legal}</p></body></html>"
    return HttpResponse(documento)  