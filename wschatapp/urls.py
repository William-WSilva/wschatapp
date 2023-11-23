from django.urls import path
from wschatapp.views import \
    Login, Cadastro, PerfilPessoal, \
    PerfilUsuario, Config, Rede, \
    PostSalvo, MeuPost, NovoPost

urlpatterns = [
    path("login/", Login, name='login'),
    path("cadastro/", Cadastro, name='cadastro'),
    path("perfil-pessoal/", PerfilPessoal, name='perfil-pessoal'),
    path("perfil-usuario/", PerfilUsuario, name='perfil-usuario'),
    path("config/", Config, name='config'),
    path("rede/", Rede, name='rede'),
    path("post-salvo/", PostSalvo, name='post-salvo'),
    path("meu-post/", MeuPost, name='meu-post'),
    path("novo-post/", NovoPost, name='novo-post'),
]