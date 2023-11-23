from django.urls import path
from wschatapp.views import Login, Cadastro

urlpatterns = [
    path("login/", Login),
     path("cadastro/", Cadastro)
]