from .models import GroceryItem
from rest_framework import generics
from .serializers import GroceryItemSerializer

class GroceryListCreateView(generics.ListCreateAPIView):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer

class GroceryItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer