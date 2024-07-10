from django.db import models

# Create your models here.

class Category(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(blank=True, null=True, max_length=50)
    def __str__(self):
        return self.nombre
    
class Product(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Customer(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=50)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} - {self.telefono}'

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    id_transaccion = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id_transaccion)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    fecha_anadida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} of {self.producto.nombre}'