from django.urls import path
from main import views

urlpatterns=[
    path('principal/',views.principal, name='principal'),
    path('principalEn/',views.principalEn, name='principalEn'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('portfolioEn/',views.portfolioEn, name='portfolioEn'),
    path('contacto/',views.contacto, name='contacto'),
    path('contactoEn/',views.contactoEn, name='contactoEn'),
]