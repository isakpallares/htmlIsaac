from django.urls import path
from . import views
urlpatterns = [
    path('hello-world/',views.hello_world,name='hello_world'),
    path('bye-world/',views.bye_world,name='bye_world'),
]
