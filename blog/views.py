from django.shortcuts import render, redirect
from blog.models import *
from .forms import *

def home(request):
    return render(request, "blog/home.html")

def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes_list")
    else:
        form = ClienteForm()

    return render(request, "blog/forms.html", {"form": form, "titulo": "Registrar Cliente"})


def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProductoForm()

    return render(request, "blog/forms.html", {"form": form, "titulo": "Registrar Producto"})

def crear_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PedidoForm()

    return render(request, "blog/forms.html", {"form": form, "titulo": "Crear Pedido"})

def buscar_cliente(request):
    resultados = []
    form = BusquedaClienteForm(request.GET or None)

    if form.is_valid():
        nombre = form.cleaned_data.get("nombre")
        if nombre:
            resultados = Cliente.objects.filter(nombre__icontains=nombre)

    contexto = {
        "form": form,
        "resultados": resultados
    }

    return render(request, "blog/busqueda.html", contexto)


def clientes_list(request):
    nombre = request.GET.get("nombre")
    clientes_query = Cliente.objects.all()
    
    if nombre is not None:
        clientes_query = Cliente.objects.filter(
            nombre__icontains=nombre
        )
    

    contexto = {
        "clientes_list": list(clientes_query)   
    }
    
    return render(request, "blog/clientes_list.html", contexto)

def productos_list(request):
    nombre = request.GET.get("nombre")
    productos_query = Producto.objects.all()
    
    if nombre is not None:
        productos_query = Producto.objects.filter(
            nombre__icontains=nombre
        )

    contexto = {
        "productos_list": list(productos_query)   
    }
    
    return render(request, "blog/productos_list.html", contexto)

def pedidos_list(request):
    cliente = request.GET.get("cliente")
    pedidos_query = Pedido.objects.all()

    if cliente is not None:
        pedidos_query = Pedido.objects.filter(
            cliente__nombre__icontains=cliente
        )

    contexto = {
        "pedidos_list": list(pedidos_query)
    }
    
    return render(request, "blog/pedidos_list.html", contexto)