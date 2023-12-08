from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Categoria

# Create your views here.

    
def inicio(request):
    productos= Producto.objects.all()
    categorias=Categoria.objects.all()
    data={
        'productos':productos,
        'categorias':categorias
    }

    return render(request,"./paginas/index.html", data)
def login(request):
    return render(request,"./paginas/login-register.html")
