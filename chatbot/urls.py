from django.urls import path
from .views import chat_home, mensaje_chat

app_name = 'chatbot'

urlpatterns = [
    path('', chat_home, name='chat_home'),
    path('mensaje_chat/', mensaje_chat, name='mensaje_chat'),
]