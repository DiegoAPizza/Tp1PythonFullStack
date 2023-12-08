from django.shortcuts import render
from django.http import HttpResponse
from .models import Servicio

# Create your views here.

    
def inicio(request):
    servicios= Servicio.objects.all()
    data={
        'servicios':servicios
    }
    return render(request,"./paginas/index.html", data)
def login(request):
    return render(request,"./paginas/login-register.html")
