from django.shortcuts import render, HttpResponse
from carro.carro import Carro
from .models import Producto



# Create your views here.


def home(request):
    
    carro= Carro(request)

    return render(request,"ProyectoWebApp/home.html")

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/listar_productos.html', {'productos': productos})

def tienda(request):
    # Lógica de la vista 'tienda'
    return render(request, 'tienda/tienda.html')






