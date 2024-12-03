from django import forms
from .models import Comida

class ComidaForm(forms.ModelForm):
    class Meta:
        model = Comida
        fields = ['nombre', 'tipo_comida', 'calorias', 'carbohidratos', 'proteinas', 'grasas']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'tipo_comida': forms.Select(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'calorias': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'carbohidratos': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'proteinas': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'grasas': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
        }