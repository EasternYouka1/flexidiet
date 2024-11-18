from django import forms

genero = (("1", "Hombre"), 
          ("2", "Mujer"))

nivel_actividad = (("1", "Sedentario"), 
                  ("2", "Moderado"), 
                  ("3", "Activo"), 
                  ("4", "Muy Activo"))

preferencias_alimentarias = (("1", "Vegetarianos"), 
                          ("2", "Veganos"), 
                          ("3", "Gluten-free"), 
                          ("4", "Lactosa"),)


class primer_setup(forms.Form):
    edad = forms.IntegerField(min_value=0, max_value=120)
    peso = forms.FloatField(min_value=20, max_value=300)
    altura = forms.FloatField(min_value=50, max_value=250)
    litros_dia = forms.IntegerField(min_value=0, max_value=200)
    comidas_dia = forms.IntegerField(min_value=0, max_value=20)
    preferencias_alimentarias = forms.ChoiceField(choices=preferencias_alimentarias)
    nivel_actividad = forms.ChoiceField(choices=nivel_actividad)
    genero = forms.ChoiceField(choices=genero)

    def __init__(self, *args, **kwargs):
        super(primer_setup, self).__init__(*args, **kwargs)
        self.fields['edad'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese su edad'
        })
        self.fields['peso'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese su peso en kg'
        })
        self.fields['altura'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese su altura en cm'
        })
        self.fields['nivel_actividad'].widget.attrs.update({'class': 'form-control'})
        self.fields['genero'].widget.attrs.update({'class': 'form-control'})
        self.fields['litros_dia'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese la cantidad de litros de agua que consume diariamente'
        })
        
        self.fields['comidas_dia'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese la cantidad de comidas que consume diariamente'
        })
        self.fields['preferencias_alimentarias'].widget.attrs.update({'class': 'form-control'})
         
         
        
       
       
        
