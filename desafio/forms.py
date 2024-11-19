from django import forms
from .models import NutritionGoal, Meal

class NutritionGoalForm(forms.ModelForm):
    class Meta:
        model = NutritionGoal
        fields = ['daily_calories', 'daily_carbs', 'daily_protein', 'daily_fat', 'water_glasses']
        widgets = {
            'daily_calories': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'daily_carbs': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'daily_protein': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'daily_fat': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'water_glasses': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
        }

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'meal_type', 'calories', 'carbs', 'protein', 'fat']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'meal_type': forms.Select(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'calories': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'carbs': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'protein': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'fat': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
        }