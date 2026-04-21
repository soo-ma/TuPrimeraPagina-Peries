from django.urls import path
from blog import views

urlpatterns = [
    path("", views.home, name="home"),
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('cliente/', views.crear_cliente, name='crear_cliente'),
    path('buscar/', views.buscar_cliente, name='buscar_cliente'),
    path('crearproducto/', views.crear_producto, name='crear_producto'),
    path('crearpedido/', views.crear_pedido, name='crear_pedido'),
    path('productos/', views.productos_list, name='productos_list'),
    path('pedidos/', views.pedidos_list, name='pedidos_list'),
]
