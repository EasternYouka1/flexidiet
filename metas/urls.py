from django.contrib import admin
from django.urls import path, include
from .views import metas_view

urlpatterns = [
    path('metas/', metas_view, name='metas'), 
]