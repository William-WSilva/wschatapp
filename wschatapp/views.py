from itertools import chain
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from wschatapp.models import Post, Rede, UsuarioInfo


def PerfilPessoal(request):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')

    usuario = request.user
    usuario_info = UsuarioInfo.objects.get(usuario=request.user)
    
    # Minhas postagens
    minhas_postagens = Post.objects.filter(usuario=usuario)

    # Lista de usuarios que sigo
    usuarios_seguidos = Rede.objects.filter(usuario=usuario).values_list('seguido', flat=True)

    # postagens de quem sigo
    postagens_seguidos = Post.objects.filter(usuario__in=usuarios_seguidos)

    # Minhas postagens + postagens de quem sigo, ordenadas por data e hora
    posts = sorted(list(chain(minhas_postagens, postagens_seguidos)), key=lambda post: post.data_hora, reverse=True)
    return render(request, 'wschatapp/perfil-pessoal.html', {'posts': posts, 'usuario_info': usuario_info, 'usuario': usuario})


def PerfilUsuario(request, user_id):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    user = get_object_or_404(User, pk=user_id)
    postsuser = Post.objects.filter(usuario=user)
    usuario_info = UsuarioInfo.objects.get(usuario=user)
    return render(request, 'wschatapp/perfil-usuario.html', {'postsuser': postsuser, 'usuario_info': usuario_info, 'user': user})


def Config(request):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    return render(request, 'wschatapp/config.html')


def MinhaRede(request):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    usuario = request.user
    seguidores = Rede.objects.filter(usuario=usuario).select_related('seguidor')
    seguidos = Rede.objects.filter(usuario=usuario).select_related('seguido')
    return render(request, 'wschatapp/rede.html', {'seguidos': seguidos,'seguidores': seguidores, 'usuario':usuario})


def PostItem(request, post_id):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    postitem = get_object_or_404(Post, pk=post_id)
    return render(request, 'wschatapp/postitem.html', {'postitem': postitem})


def PostSalvo(request):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    return render(request, 'wschatapp/post-salvo.html')


def MeuPost(request):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    return render(request, 'wschatapp/meu-post.html')


def NovoPost(request):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    return render(request, 'wschatapp/novo-post.html')