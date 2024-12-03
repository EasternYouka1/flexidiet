from django.urls import path
from .views import dieta, dashboard, editar_comida, eliminar_comida

urlpatterns = [
    path('dieta/', dieta, name='dieta'), 
    path('dashboard/', dashboard, name='dashboard'),
    path('editar_comida/<int:comida_id>/', editar_comida, name='editar_comida'),
    path('eliminar_comida/<int:comida_id>/', eliminar_comida, name='eliminar_comida'),
]