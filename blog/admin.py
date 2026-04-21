from django.contrib import admin
from blog.models import Cliente, Producto, Pedido

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "edad", "mail",)

    list_display_links = ("nombre",)

    search_fields = ("nombre",)

    list_filter = ("edad",)

    ordering = ("nombre",)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "stock")

    list_display_links = ("nombre",)

    search_fields = ("nombre",)

    list_filter = ("stock",)

    ordering = ("nombre", "stock",)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("producto", "cantidad", "cliente", "fecha")

    list_display_links = ("producto",)

    search_fields = ("nombre", "cliente",)

    list_filter = ("producto",)

    ordering = ("fecha",)

