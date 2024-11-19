from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meal(models.Model):
    MEAL_TYPES = [
        ('desayuno', 'Desayuno'),
        ('almuerzo', 'Almuerzo'),
        ('cena', 'Cena'),
        ('snack', 'Snack')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    calories = models.IntegerField()
    carbs = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    date = models.DateField(auto_now_add=True)
