from django.shortcuts import render, redirect
from blog.models import *
from .forms import *

def home(request):
    return render(request, "blog/home.html")

def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("clientes_list")

    return render(request, "blog/forms.html", {"form": form, "titulo": "Registrar Cliente"})


def crear_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "blog/forms.html", {"form": form, "titulo": "Registrar Producto"})

def crear_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")

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
    clientes_query = Cliente.objects.all()
    
    contexto = {
        "clientes_list": list(clientes_query)   
    }
    
    return render(request, "blog/clientes_list.html", contexto)

