from django.db import models
from uuid import uuid4
# Create your models here.
class Servicio(models.Model):
    idServicio=models.AutoField(primary_key=True)
    
    # Definir el modelo para Servicio
class MetodoDePago(models.Model):
    idCliente=models.AutoField(primary_key=True)
    
class MetodoDeCobro(models.Model):
   idCliente=models.AutoField(primary_key=True)
   
class Producto(models.Model):
    idProducto=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=45)
    cantidad=models.IntegerField(max_length=200)
    imagen=models.ImageField(upload_to='imagenes/',null=True,blank=True)
    
class Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=45)
    apellido=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    idServicio=models.ForeignKey(Servicio, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idMetodoDePago=models.ForeignKey(MetodoDePago,on_delete=models.CASCADE)
    idMetodoDeCobro=models.ForeignKey(MetodoDeCobro,on_delete=models.CASCADE)

    
    