from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Categoria, Blog

# Create your views here.

    
def inicio(request):
    productos= Producto.objects.all()
    categorias=Categoria.objects.all()
    blogs= Blog.objects.all()
    data={
        'productos':productos,
        'categorias':categorias,
        'blogs':blogs
    }

    return render(request,"./paginas/index.html", data)
def login(request):
    return render(request,"./paginas/login-register.html")

def service(request):
    return render(request,"./servicios/crear.html")

def edit(request):
    return render(request,"./servicios/editar.html")

