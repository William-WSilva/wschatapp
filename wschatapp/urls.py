from django.urls import path
from wschatapp.views import \
    PerfilPessoal, \
    PerfilUsuario, Config, MinhaRede, \
    PostsSalvos, SalvarPost, MeusPosts, \
    NovoPost, PostItem, BuscarUsuarios, \
    SeguirUsuario, NaoSeguirUsuario, NaoSalvarPost, ComentarPost, CurtirPost

urlpatterns = [
    path("perfil-pessoal/", PerfilPessoal, name='perfil-pessoal'),
    path("config/", Config, name='config'),
    path("rede/", MinhaRede, name='rede'),
    path("buscar-usuarios/", BuscarUsuarios, name='buscar-usuarios'),
    path("posts-salvos/", PostsSalvos, name='posts-salvos'),
    path("meus-posts/", MeusPosts, name='meus-posts'),
    path("novo-post/", NovoPost, name='novo-post'),
    path("perfil-usuario/<int:user_id>", PerfilUsuario, name='perfil-usuario'),
    path("post-item/<int:post_id>", PostItem, name='post-item'),
    path("seguir-usuario/<int:user_id>", SeguirUsuario, name='seguir-usuario'),
    path("nao-seguir-usuario/<int:user_id>", NaoSeguirUsuario, name='nao-seguir-usuario'),
    path("salvar-post/<int:post_id>", SalvarPost, name='salvar-post'),
    path("nao-salvar-post/<int:post_id>", NaoSalvarPost, name='nao-salvar-post'),
    path("comentar-post/<int:post_id>", ComentarPost, name='comentar-post'),
    path("curtir-post/<int:post_id>", CurtirPost, name='curtir-post'),
]