from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({'message':'Hola desde el Backend'})
@api_view(['GET'])
def bye_world(request):
    return Response({'message':'adios desde el Backend'})
