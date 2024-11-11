from django.urls import path
from .views import primer_login  

urlpatterns = [
    path('setup/', primer_login, name="primer_setup"),  # Change the view function name
]