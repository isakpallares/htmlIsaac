"""
URL configuration for proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from proyecto1.views import saludo, despedida, dame_fecha, saludopersonal, calcula_edad, calcula_edad_futura, saludo_personalizado, perfil_usuario, calcular_hipotenusa, mayor_edad
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('despedida/',despedida),
    path('fecha/',dame_fecha),    
    path('saludopersonal/<int:numero>/', saludopersonal),
    path('edades/<int:anio>/', calcula_edad),
    path('edadesfutura/<int:edad_actual>/<int:anio>/',calcula_edad_futura),
    path('saludopersonalizado/<str:nombre>/',saludo_personalizado),
    path('perfilusuario/<str:usuario>/<str:seccion>/',perfil_usuario),
    path('calcularhipotenusa/<int:lado_a>/<int:lado_b>/',calcular_hipotenusa),
    path('mayoredad/<int:edad>/',mayor_edad),
]