from django import forms
from blog.models import Cliente, Producto, Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ("nombre", "edad", "mail")
        labels = {
            "nombre": "Nombre",
            "edad": "Edad",
            "mail": "Correo electrónico"
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ("nombre", "precio", "stock")


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ("cliente", "producto", "cantidad")


class BusquedaClienteForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        required=False,
        label="Buscar cliente por nombre"
    )