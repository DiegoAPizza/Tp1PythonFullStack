from django.db import models
from uuid import uuid4
from decimal import Decimal

class Categoria(models.Model):
    idCat = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=100)
    clase_css = models.CharField(max_length=50, blank=True, null=True)
    

class Servicio(models.Model):
    idServicio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    precio = models.IntegerField()
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=0)

class MetodoDePago(models.Model):
    idPago = models.AutoField(primary_key=True)
    tipoMetPag = models.CharField(max_length=30, default=' ')

class MetodoDeCobro(models.Model):
    idMetod = models.AutoField(primary_key=True)
    tipoMet = models.CharField(max_length=30, default=1) 
    idServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, default=1)




class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    categoria = models.CharField(max_length=70, default='default_value')
    desc=models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_precio_con_descuento(self):
        descuento = (self.desc / Decimal('100')) * self.precio
        precio_con_descuento = self.precio - descuento
        precio_con_descuento = precio_con_descuento.quantize(Decimal('0.00'))
        return precio_con_descuento

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f}"
    
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    descripcion = models.TextField(max_length=299)
    icono_1 = models.CharField(max_length=50, default='fa-solid fa-star')
    icono_2 = models.CharField(max_length=50, default='fa-solid fa-heart')
    icono_3 = models.CharField(max_length=50, default='fa-solid fa-star')
    icono_4 = models.CharField(max_length=50, default='fa-solid fa-heart')
    icono_5 = models.CharField(max_length=50, default='fa-solid fa-circle')



class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    idServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idMetodoDePago = models.ForeignKey(MetodoDePago, on_delete=models.CASCADE)
    idMetodoDeCobro = models.ForeignKey(MetodoDeCobro, on_delete=models.CASCADE)
