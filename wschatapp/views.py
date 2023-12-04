from itertools import chain
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from usuarios.forms import CadastroForms
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
    
    usuario = request.user
    usuario_info = UsuarioInfo.objects.get(usuario=usuario)

    # Preenche o formulário com os dados do usuário
    form = CadastroForms(request.POST or None, initial={
        'nome_usuario': usuario.username,
        'sobrenome': usuario.last_name,
        'email': usuario.email,
    })
    senha_form = PasswordChangeForm(user=usuario)

    if request.method == 'POST':
        form = CadastroForms(request.POST, request.FILES)

        if form.is_valid():
            usuario.username = form.cleaned_data['nome_usuario']
            usuario.last_name = form.cleaned_data['sobrenome']
            usuario.email = form.cleaned_data['email']
            nova_senha = form.cleaned_data['senha']
            
            if nova_senha:
                usuario.set_password(nova_senha)
                usuario.save()
            else:
                usuario.save()

           # Atualiza a imagem de perfil na tabela UsuarioInfo
            foto_perfil = request.FILES.get('foto_perfil')
            if foto_perfil:
                usuario_info.foto_perfil = foto_perfil
                usuario_info.save()

            # Atualiza a sessão do usuário após a alteração de senha
            update_session_auth_hash(request, usuario)

            messages.success(request, 'Informações atualizadas com sucesso')
            return redirect('config')

    return render(request, 'wschatapp/config.html', {'usuario_info': usuario_info, 'form': form, 'usuario': usuario})


def MinhaRede(request):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    usuario = request.user
    usuario_info = UsuarioInfo.objects.get(usuario=usuario)
    seguidores = Rede.objects.filter(usuario=usuario).select_related('seguidor')
    seguidos = Rede.objects.filter(usuario=usuario).select_related('seguido')

    return render(request, 'wschatapp/rede.html', {'seguidos': seguidos,'seguidores': seguidores, 'usuario':usuario, 'usuario_info': usuario_info})


def PostItem(request, post_id):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    postitem = get_object_or_404(Post, pk=post_id)

    usuario = request.user
    usuario_info = UsuarioInfo.objects.get(usuario=usuario)

    return render(request, 'wschatapp/postitem.html', {'postitem': postitem})


def PostSalvo(request):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    usuario = request.user
    usuario_info = UsuarioInfo.objects.get(usuario=usuario)

    return render(request, 'wschatapp/post-salvo.html')


def MeusPosts(request):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    usuario = request.user
    usuario_info = UsuarioInfo.objects.get(usuario=usuario)
    posts = Post.objects.filter(usuario=usuario)
    return render(request, 'wschatapp/meus-posts.html', {'posts': posts, 'usuario_info': usuario_info, 'usuario': usuario})


def NovoPost(request):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    usuario = request.user
    usuario_info = UsuarioInfo.objects.get(usuario=usuario)

    return render(request, 'wschatapp/novo-post.html')