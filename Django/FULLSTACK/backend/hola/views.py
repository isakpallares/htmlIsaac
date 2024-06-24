from django.shortcuts import render # type: ignore
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore



@api_view(['GET'])
def hello_world(request):
    return Response({'message':'Hola desde el backend'})
