from django.db import models
from django.contrib.auth.models import User

class NutritionGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    daily_calories = models.IntegerField(default=2000)
    daily_carbs = models.IntegerField(default=250)  # en gramos
    daily_protein = models.IntegerField(default=60)  # en gramos
    daily_fat = models.IntegerField(default=70)     # en gramos
    water_glasses = models.IntegerField(default=8)

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

class WaterIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    glasses = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)