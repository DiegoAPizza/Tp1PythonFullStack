from django.db import models
from uuid import uuid4
# Create your models here.
class Tarea(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid4,editable=False)
    nombre = models.CharField(max_length=200)
    class Meta:
        verbose_name='Tarea'
        verbose_name_plural='Tareas'
        db_table='Tarea'
    