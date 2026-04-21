from django.urls import path
from blog import views

urlpatterns = [
    path("", views.home, name="home"),
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('cliente/', views.crear_cliente, name='crear_cliente'),
    path('buscar/', views.buscar_cliente, name='buscar_cliente'),
    path('producto/', views.crear_producto, name='crear_producto'),
    path('pedido/', views.crear_pedido, name='crear_pedido'),
]
