from django.contrib import messages
from django import forms
from .models import NutritionGoal



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
        
        
        
