from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dieta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_dieta = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo_dieta = models.CharField(max_length=50)
    activa = models.BooleanField(default=True)