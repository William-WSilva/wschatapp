from django.urls import path
from wschatapp.views import \
    PerfilPessoal, \
    PerfilUsuario, Config, MinhaRede, \
    PostsSalvos, SalvarPost, MeusPosts, \
    NovoPost, PostItem, BuscarUsuarios, SeguirUsuario, NaoSeguirUsuario

urlpatterns = [
    path("perfil-pessoal/", PerfilPessoal, name='perfil-pessoal'),
    path("perfil-usuario/<int:user_id>", PerfilUsuario, name='perfil-usuario'),
    path("seguir-usuario/<int:user_id>", SeguirUsuario, name='seguir-usuario'),
    path("nao-seguir-usuario/<int:user_id>", NaoSeguirUsuario, name='nao-seguir-usuario'),
    path("config/", Config, name='config'),
    path("rede/", MinhaRede, name='rede'),
    path("buscar-usuarios/", BuscarUsuarios, name='buscar-usuarios'),
    path("posts-salvos/", PostsSalvos, name='posts-salvos'),
    path("salvar-post/<int:post_id>", SalvarPost, name='salvar-post'),
    path("meus-posts/", MeusPosts, name='meus-posts'),
    path("novo-post/", NovoPost, name='novo-post'),
    path("post-item/<int:post_id>", PostItem, name='post-item'),
]