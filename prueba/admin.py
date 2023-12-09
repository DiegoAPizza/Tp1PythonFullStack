from django.contrib import admin

# Register your models here.
from .models import Servicio, MetodoDeCobro, MetodoDePago, Categoria, Producto, Cliente, Blog

#Register your models here.
admin.site.register(Servicio)
admin.site.register(MetodoDeCobro)
admin.site.register(MetodoDePago)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Blog)