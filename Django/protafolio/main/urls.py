from django.urls import path
from main import views

urlpatterns=[
    path('principal/',views.principal, name='principal'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('contacto/',views.contacto, name='contacto'),
]