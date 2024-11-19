from django.db import models

# Create your models here.
class desafio_diario(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    puntos = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre
    
class desafio_semanal(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    puntos = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre
    
class desfaio_mensual(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    puntos = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre

class Logro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    puntos = models.IntegerField()
    imagen = models.ImageField(upload_to="logros", null=True, blank=True)
    fecha_obtenido = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
