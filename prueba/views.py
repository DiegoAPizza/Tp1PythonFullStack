from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request,"./paginas/index.html")
def login(request):
    return render(request,"./paginas/login.html")
def login_prueba(request):
    return render(request,"./paginas/login_prueba.html")