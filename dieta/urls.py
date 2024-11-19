
from django.contrib import admin
from django.urls import path, include
from .views import dieta_view



urlpatterns = [
    path('dieta/', dieta_view , name='dieta'), 
]