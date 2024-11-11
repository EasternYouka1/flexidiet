from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import primer_setup 
import logging
from .models import info_usuario

logger = logging.getLogger(__name__)

@login_required
def primer_login(request):
    # Verificar si el usuario ya tiene perfil y si no es su primer login
    try:
        user_info = info_usuario.objects.get(user=request.user)
        if not user_info.primer_login:
            messages.info(request, "Ya has completado tu configuración inicial")
            return redirect('login:home')
    except info_usuario.DoesNotExist:
        # Si no existe, continuamos con el formulario
        pass

    if request.method == "POST":
        form = primer_setup(request.POST)
        if form.is_valid():
            try:
                # Creamos un nuevo registro o actualizamos el existente
                info_usuario.objects.update_or_create(
                    user=request.user,
                    defaults={
                        'edad': form.cleaned_data['edad'],
                        'peso': form.cleaned_data['peso'],
                        'altura': form.cleaned_data['altura'],
                        'nivel_actividad': form.cleaned_data['nivel_actividad'],
                        'genero': form.cleaned_data['genero'],
                        'primer_login': False
                    }
                )
                
                logger.info(f"Setup completed for user {request.user.username}")
                messages.success(request, "¡Configuración inicial completada con éxito!")
                return redirect('login:home')
            except Exception as e:
                logger.error(f"Error saving user setup: {str(e)}")
                messages.error(request, "Hubo un error al guardar tu información")
        else:
            logger.warning(f"Invalid form submission for user {request.user.username}")
            logger.debug(f"Form errors: {form.errors}")
    else:
        # Si el usuario ya tiene un perfil, prellenamos el formulario
        try:
            user_info = info_usuario.objects.get(user=request.user)
            initial_data = {
                'edad': user_info.edad,
                'peso': user_info.peso,
                'altura': user_info.altura,
                'nivel_actividad': user_info.nivel_actividad,
                'genero': user_info.genero
            }
            form = primer_setup(initial=initial_data)
        except info_usuario.DoesNotExist:
            form = primer_setup()
    
    return render(request, "primer_login/setup.html", {"form": form})