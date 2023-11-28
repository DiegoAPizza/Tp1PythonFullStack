from django.db import models
from uuid import uuid4
# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=256, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=1024)
   # img=models.ImageField("")##Ruta de la Imgane
class Servicio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nombre = models.CharField(max_length=256, unique=True)
    