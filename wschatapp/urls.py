from django.urls import path
from wschatapp.views import \
    PerfilPessoal, \
    PerfilUsuario, Config, Rede, \
    PostSalvo, MeuPost, NovoPost, PostItem

urlpatterns = [
    path("perfil-pessoal/", PerfilPessoal, name='perfil-pessoal'),
    path("perfil-usuario/<int:user_id>/", PerfilUsuario, name='perfil-usuario'),
    path("config/", Config, name='config'),
    path("rede/", Rede, name='rede'),
    path("post-salvo/", PostSalvo, name='post-salvo'),
    path("meu-post/", MeuPost, name='meu-post'),
    path("novo-post/", NovoPost, name='novo-post'),
    path("post-item/<int:post_id>", PostItem, name='post-item'),
]