from django.db import models
from uuid import uuid4


class Categoria(models.Model):
    idCat = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=100)
    
    

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
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    descripcion = models.TextField(max_length=299)

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    idServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idMetodoDePago = models.ForeignKey(MetodoDePago, on_delete=models.CASCADE)
    idMetodoDeCobro = models.ForeignKey(MetodoDeCobro, on_delete=models.CASCADE)
