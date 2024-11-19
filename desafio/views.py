from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import date
from .models import NutritionGoal, Meal, WaterIntake




@login_required
def dashboard(request):

    goals = NutritionGoal.objects.get_or_create(user=request.user)[0]
    
    # Obtener comidas del día
    today = date.today()
    daily_meals = Meal.objects.filter(user=request.user, date=today)
    
    # Calcular totales del día
    totals = daily_meals.aggregate(
        calories=Sum('calories'),
        carbs=Sum('carbs'),
        protein=Sum('protein'),
        fat=Sum('fat')
    )
    
    # Obtener ingesta de agua
    water_intake = WaterIntake.objects.get_or_create(user=request.user, date=today)[0]
    
    # Calcular porcentajes
    calories_percent = (totals['calories'] or 0) / goals.daily_calories * 100 if goals.daily_calories else 0
    water_percent = (water_intake.glasses / goals.water_glasses * 100) if goals.water_glasses else 0
    
    context = {
        'goals': goals,
        'totals': totals,
        'water_intake': water_intake,
        'calories_percent': calories_percent,
        'water_percent': water_percent,
        'daily_meals': daily_meals,
    }
    
    return render(request, 'dashboard/dashboard.html', context)
