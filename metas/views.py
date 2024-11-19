from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import NutritionGoal
from .forms import NutritionGoalForm
from django.contrib import messages




@login_required
def metas_view(request):
    # Obtener o crear metas del usuario
    goals, created = NutritionGoal.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = NutritionGoalForm(request.POST, instance=goals)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, 'Metas actualizadas correctamente')
            return redirect('metas:metas')
    else:
        form = NutritionGoalForm(instance=goals)
    
    context = {
        'form': form,
        'goals': goals
    }
    return render(request, 'modulos/metas.html', context)

