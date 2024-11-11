from django.db import models
from django.contrib.auth.models import User


class info_usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    peso = models.FloatField()
    edad = models.IntegerField()
    altura = models.FloatField()
    nivel_actividad = models.CharField(max_length=50)
    primer_login = models.BooleanField(default=True)
    genero = models.CharField(max_length=1)
    fecha_registro = models.DateField(auto_now_add=True)