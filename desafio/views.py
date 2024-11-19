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


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import NutritionGoal, Meal
from .forms import NutritionGoalForm, MealForm
from django.db.models import Sum
from datetime import date

@login_required
def metas(request):
    # Obtener o crear metas del usuario
    goals, created = NutritionGoal.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = NutritionGoalForm(request.POST, instance=goals)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, 'Metas actualizadas correctamente')
            return redirect('metas')
    else:
        form = NutritionGoalForm(instance=goals)
    
    context = {
        'form': form,
        'goals': goals
    }
    return render(request, 'nutrition/metas.html', context)

@login_required
def dieta(request):
    today = date.today()
    meals = Meal.objects.filter(user=request.user, date=today)
    
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.date = today
            meal.save()
            messages.success(request, 'Comida agregada correctamente')
            return redirect('dieta')
    else:
        form = MealForm()
    
    # Calcular totales del día
    totals = meals.aggregate(
        calories=Sum('calories'),
        carbs=Sum('carbs'),
        protein=Sum('protein'),
        fat=Sum('fat')
    )
    
    context = {
        'form': form,
        'meals': meals,
        'totals': totals
    }
    return render(request, 'nutrition/dieta.html', context)

@login_required
def eliminar_comida(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id, user=request.user)
    meal.delete()
    messages.success(request, 'Comida eliminada correctamente')
    return redirect('dieta')

@login_required
def editar_comida(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id, user=request.user)
    
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comida actualizada correctamente')
            return redirect('dieta')
    else:
        form = MealForm(instance=meal)
    
    context = {
        'form': form,
        'meal': meal
    }
    return render(request, 'nutrition/editar_comida.html', context)
