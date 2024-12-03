from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("login.urls", "login"), namespace="login")),
    path("", include(("info_usuarios.urls", "info_usuarios"), namespace="info_usuarios")),
    path("", include(("metas.urls", "metas"), namespace="metas")),
    path("", include(("dieta.urls", "dieta"), namespace="dieta")),
    path("chatbot/", include(("chatbot.urls", "chatbot"), namespace="chatbot")),
]