from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from wschatapp.models import Post, Rede, UsuarioInfo


@login_required
def PerfilPessoal(request):
    usuario_info = UsuarioInfo.objects.get(usuario=request.user)
    usuario = request.user  # Obtém o usuário logado
    usuarios_seguidos = Rede.objects.filter(seguidor=usuario).values_list('seguido', flat=True)
    posts = Post.objects.filter(usuario__in=usuarios_seguidos)
    return render(request, 'wschatapp/perfil-pessoal.html', {'posts': posts, 'usuario_info': usuario_info})

def PerfilUsuario(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    postsuser = Post.objects.filter(usuario=user)
    usuario_info = UsuarioInfo.objects.get(usuario=user)
    return render(request, 'wschatapp/perfil-usuario.html', {'postsuser': postsuser, 'usuario_info': usuario_info, 'user': user})

def Config(request):
    return render(request, 'wschatapp/config.html')

def ExibirRede(request):
    return render(request, 'wschatapp/rede.html')

def PostItem(request, post_id):
    postitem = get_object_or_404(Post, pk=post_id)
    return render(request, 'wschatapp/postitem.html', {'postitem': postitem})

def PostSalvo(request):
    return render(request, 'wschatapp/post-salvo.html')

def MeuPost(request):
    return render(request, 'wschatapp/meu-post.html')

def NovoPost(request):
    return render(request, 'wschatapp/novo-post.html')