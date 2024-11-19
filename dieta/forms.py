from django import forms
from .models import Meal



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