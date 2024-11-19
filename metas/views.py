from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def metas_view(request):
    return render(request, "modulos/metas.html", {})

