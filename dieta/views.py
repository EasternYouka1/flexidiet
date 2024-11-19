from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dieta_view(request):
    return render(request, "modulos/dieta.html", {})



# Create your views here.
