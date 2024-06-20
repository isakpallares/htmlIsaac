from django.contrib import admin

# Register your models here.
from Aplicacion1.models import Category, Product, Customer, Order, OrderItem

class CategoryAdmin(admin.ModelAdmin):
    list_display=("nombre", "descripcion")
    search_fields=('nombre','descripcion')
    list_filter=('nombre',) #No olvidar Coma
    
class ProductAdmin(admin.ModelAdmin):
    list_display=("nombre", "precio",'stock','categoria')
    search_fields=('nombre','categoria')
    list_filter=('nombre',) #No olvidar Coma
    
class CustomerAdmin(admin.ModelAdmin):
    list_display=("nombre", "email",'telefono')
    search_fields=('nombre','telefono')
    list_filter=('nombre',) #No olvidar Coma
    
class OrderAdmin(admin.ModelAdmin):
    list_display=("customer", "fecha_pedido",'completado','id_transaccion')
    search_fields=('customer','id_transaccion')
    list_filter=('id_transaccion',) #No olvidar Coma
    
class OrderItemAdmin(admin.ModelAdmin):
    list_display=("order", "producto",'cantidad','fecha_anadida')
    search_fields=('order','producto')
    list_filter=('order',) #No olvidar Coma
    
    

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
    