
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("principal/", include('main.urls')),
    path("principal/En", include('main.urls')),
    path("portfolio/", include('main.urls')),
    path("portfolioEn/", include('main.urls')),
    path("contacto/", include('main.urls')),
    path("contactoEn/", include('main.urls')),
    
]
