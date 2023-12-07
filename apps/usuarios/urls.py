from django.urls import path
from apps.usuarios.views import home, login, cadastro, logout

urlpatterns = [
    path("", home, name='home'),
    path("login/", login, name='login'),
    path("cadastro/", cadastro, name='cadastro'),
    path("logout/", logout, name='logout')
]