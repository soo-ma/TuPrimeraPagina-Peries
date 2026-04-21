from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    mail = models.EmailField(unique=True)

    def __str__(self):
        return "nombre del cliente: " + self.nombre + ", edad: " + str(self.edad) + ", mail: " + self.mail + "."


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return "nombre del producto: " + self.nombre + ", precio: " + str(self.precio) + ", stock: " + str(self.stock) + "."
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.cliente) + "compró" + str(self.producto) + "."