from django.db import models
from django.core.exceptions import ValidationError

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    mail = models.EmailField(unique=True)

    def __str__(self):
        return "Nombre: " + self.nombre + ", edad: " + str(self.edad) + ", mail: " + self.mail + "."


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()

    def clean(self):
        if self.stock < 1:
            raise ValidationError("La cantidad debe ser al menos 1.")
        if self.precio < 0:
            raise ValidationError("El precio debe ser mayor a 0.")

    def __str__(self):
        return "Nombre: " + self.nombre + ", precio: " + str(self.precio) + ", stock: " + str(self.stock) + "."
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    fecha = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.cantidad > self.producto.stock:
            raise ValidationError("No hay suficiente stock para este pedido.")
        if self.cantidad < 1:
            raise ValidationError("La cantidad debe ser al menos 1.")

    def __str__(self):
        return str(self.cliente.nombre) + " compró " + str(self.cantidad) + " " + str(self.producto.nombre) + "."