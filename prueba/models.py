from django.db import models
from uuid import uuid4
# Create your models here.
class Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=45)
    apellido=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    idServicio=models.ForeignKey()
    idProducto=models.ForeignKey()
    idMetodoDePago=models.ForeignKey(to=Producto)
    idMetodoDeCobro=models.ForeignKey()
class Producto(models.Model):
    idProducto=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=45)
    cantidad=models.IntegerField(max_length=200)
    imagen=models.ImageField(upload_to='imagenes/',null=True,blank=True)
    
    