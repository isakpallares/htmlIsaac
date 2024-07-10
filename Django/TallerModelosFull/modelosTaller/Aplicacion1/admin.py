from django.contrib import admin

# Register your models here.
from Aplicacion1.models import Category, Product, Customer, Order, OrderItem

class CategoryAdmin(admin.ModelAdmin):
    list_display=("nombre", "descripcion")
    search_fields=('nombre','descripcion')
    list_filter=('nombre',)
    
class ProductAdmin(admin.ModelAdmin):
    list_display=("nombre", "precio",'stock','categoria')
    search_fields=('nombre','categoria')
    list_filter=('nombre',) 
    
class CustomerAdmin(admin.ModelAdmin):
    list_display=("nombre", "email",'telefono')
    search_fields=('nombre','telefono')
    list_filter=('nombre',) 
class OrderAdmin(admin.ModelAdmin):
    list_display=("customer", "fecha_pedido",'id_transaccion')
    search_fields=('customer','id_transaccion')
    list_filter=('id_transaccion',) 
    
class OrderItemAdmin(admin.ModelAdmin):
    list_display=("order", "producto",'cantidad','fecha_anadida')
    search_fields=('order','producto')
    list_filter=('fecha_anadida',) #No olvidar Coma

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
    