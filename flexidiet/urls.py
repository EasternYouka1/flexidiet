from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("login.urls", "login"), namespace="login")),
    path("", include(("info_usuarios.urls", "info_usuarios"), namespace="info_usuarios")),
    path("", include(("desafio.urls", "desafio"), namespace="desafio")),
    path("", include(("metas.urls", "metas"), namespace="metas")),
    path("",include(("dieta.urls", "dieta"), namespace="dieta")),
]
