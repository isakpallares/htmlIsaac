from django.urls import path
from .views import GroceryListCreateView,GroceryItemRetrieveUpdateDestroyView


urlpatterns = [
    path('groceryItems',GroceryListCreateView.as_view(),name='Cracion-listar-comestible'),
    
    path('groceryItems/<int:pk>/',GroceryItemRetrieveUpdateDestroyView.as_view(),name='recuperar-actualizar')
]
