from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MetaNutricional
from .forms import MetaNutricionalForm
from django.contrib import messages

@login_required
def metas_view(request):
    # Obtener o crear metas del usuario
    metas, creado = MetaNutricional.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        form = MetaNutricionalForm(request.POST, instance=metas)
        if form.is_valid():
            meta = form.save(commit=False)
            meta.usuario = request.user
            meta.save()
            messages.success(request, 'Metas actualizadas correctamente')
            return redirect('metas:metas')
    else:
        form = MetaNutricionalForm(instance=metas)
    
    context = {
        'form': form,
        'metas': metas
    }
    return render(request, 'modulos/metas.html', context)