from itertools import chain
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from usuarios.forms import CadastroForms
from wschatapp.models import Comentario, Curtida, Post, Rede, UsuarioInfo, PostSalvo


def PerfilPessoal(request):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')

    usuario = request.user
    usuario_info = UsuarioInfo.objects.get(usuario=request.user)
    
    # Lista de usuarios que sigo
    usuarios_seguidos = Rede.objects.filter(usuario=usuario).values_list('seguido', flat=True)
    # Minhas postagens
    minhas_postagens = Post.objects.filter(usuario=usuario)
    # postagens de quem sigo
    postagens_seguidos = Post.objects.filter(usuario__in=usuarios_seguidos)
    # Minhas postagens + postagens de quem sigo, ordenadas por data e hora
    posts = sorted(list(chain(minhas_postagens, postagens_seguidos)), key=lambda post: post.data_hora, reverse=True)
    for post in posts:post.qtd_comentarios = Comentario.objects.filter(post=post).count() # Add qtd comentarios de cada post
    for post in posts:post.qtd_curtidas = Curtida.objects.filter(post=post).count() # Add qtd comentarios de cada post

    # Verifica se o post já está salvo pelo usuário atual
    posts_salvos = PostSalvo.objects.filter(usuario=usuario).values_list('post__id', flat=True)
    # Verifica se o post já está salvo pelo usuário atual
    posts_curtidos = Curtida.objects.filter(usuario=usuario).values_list('post__id', flat=True)

    qtd_seguidos = Rede.objects.filter(usuario=usuario).exclude(seguido__isnull=True).values_list('seguido').count()
    qtd_seguidores = Rede.objects.filter(usuario=usuario).exclude(seguidor__isnull=True).values_list('seguidor').count()


    return render(request, 'wschatapp/perfil-pessoal.html', 
        {'posts': posts, 
         'usuario_info': usuario_info, 
         'usuario': usuario,
         'posts_salvos': posts_salvos,
         'posts_curtidos': posts_curtidos,
         'qtd_seguidos': qtd_seguidos,
         'qtd_seguidores': qtd_seguidores,})


def PerfilUsuario(request, user_id):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    user = get_object_or_404(User, pk=user_id)
    postsuser = Post.objects.filter(usuario=user)
    usuario_info = UsuarioInfo.objects.get(usuario=user)

    usuario_atual = request.user
    esta_seguindo = Rede.objects.filter(usuario=usuario_atual, seguido=user).exists()
    
    return render(request, 'wschatapp/perfil-usuario.html', 
        {'postsuser': postsuser, 
         'usuario_info': usuario_info, 
         'user': user, 'esta_seguindo': esta_seguindo
        }
    )



def SeguirUsuario(request, user_id):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')

    usuario_a_seguir = get_object_or_404(User, pk=user_id)
    usuario_atual = request.user
    # Verifica se o usuário atual já está seguindo o usuario_a_seguir
    if not Rede.objects.filter(usuario=usuario_atual, seguido=usuario_a_seguir).exists():
        Rede.objects.create(usuario=usuario_atual, seguido=usuario_a_seguir)

    # Redireciona de volta para o perfil do usuário que foi seguido
    return redirect('perfil-usuario', user_id=user_id)


def NaoSeguirUsuario(request, user_id):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    usuario_nao_seguir = get_object_or_404(User, pk=user_id)
    usuario_atual = request.user
    # Verifica se o usuário atual está seguindo o usuario_nao_seguir
    if Rede.objects.filter(usuario=usuario_atual, seguido=usuario_nao_seguir).exists():
        Rede.objects.filter(usuario=usuario_atual, seguido=usuario_nao_seguir).delete()

    # Redireciona de volta para o perfil do usuário que foi seguido
    return redirect('perfil-usuario', user_id=user_id)



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

    lista_seguidos = Rede.objects.filter(usuario=usuario).values_list('seguido', flat=True)
    seguidos = UsuarioInfo.objects.filter(id__in=lista_seguidos)

    lista_seguidores = Rede.objects.filter(usuario=usuario).values_list('seguidor', flat=True)
    seguidores = UsuarioInfo.objects.filter(id__in=lista_seguidores)

    return render(request, 'wschatapp/rede.html', {'seguidos': seguidos,'seguidores': seguidores, 'usuario':usuario, 'usuario_info': usuario_info})


def PostItem(request, post_id):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    post = get_object_or_404(Post, pk=post_id)
    usuario = request.user
    usuario_info = UsuarioInfo.objects.get(usuario=usuario)
    # Verifica se o post já está salvo pelo usuário atual
    posts_salvos = PostSalvo.objects.filter(usuario=usuario).values_list('post__id', flat=True)
    comentarios_post = Comentario.objects.filter(post_id=post_id).select_related('usuario__usuarioinfo')
    curtidas_post = Curtida.objects.filter(post_id=post_id).select_related('usuario__usuarioinfo')

    return render(request, 'wschatapp/post-item.html', 
        {'usuario_info': usuario_info, 
         'post': post, 
         'posts_salvos': posts_salvos,
         'comentarios_post': comentarios_post,
         'curtidas_post': curtidas_post})


def SalvarPost(request, post_id):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    # Obtém o post com base no ID recebido
    postitem = Post.objects.get(id=post_id)
    # Cria uma entrada na tabela PostSalvo para salvar o post para o usuário atual
    PostSalvo.objects.create(usuario=request.user, post=postitem)

    # Redireciona de volta para alguma página após salvar o post
    return redirect('perfil-pessoal')


def NaoSalvarPost(request, post_id):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')

    # Obtém o post salvo pelo ID do post e pelo usuário atual
    post_salvo = get_object_or_404(PostSalvo, post_id=post_id, usuario=request.user)
    post_salvo.delete() # Remove o post salvo

    return redirect('posts-salvos')


def PostsSalvos(request):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    usuario = request.user
    usuario_info = UsuarioInfo.objects.get(usuario=usuario)
    ids_posts_salvos = PostSalvo.objects.filter(usuario=usuario).values_list('post__id', flat=True) # Obtém os IDs dos posts salvos pelo usuário atual
    posts = Post.objects.filter(id__in=ids_posts_salvos) # Obtém os detalhes dos posts salvos pelo usuário atual

    return render(request, 'wschatapp/posts-salvos.html', {'usuario': usuario ,'usuario_info': usuario_info, 'posts': posts})


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


def BuscarUsuarios(request):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    usuario = request.user
    usuario_info = UsuarioInfo.objects.get(usuario=usuario)

    usuariosrede = UsuarioInfo.objects.all()

    return render(request, 'wschatapp/buscar-usuarios.html', {'usuario_info': usuario_info, 'usuario': usuario, 'usuariosrede': usuariosrede})

def ComentarPost(request, post_id):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    # Verifique se o método de requisição é POST
    if request.method == 'POST':
        # Obtenha o post relacionado ao post_id ou retorne um erro 404 se não existir
        post = get_object_or_404(Post, pk=post_id)

        # Capture o texto do comentário do formulário
        comentario_texto = request.POST.get('comentario')

        # Verifique se o campo de comentário não está vazio
        if not comentario_texto:
            messages.error(request, 'O campo de comentário está vazio.')
            return redirect('perfil-pessoal')  # Redirecione para onde for apropriado

        # Crie e salve um novo objeto Comentario
        novo_comentario = Comentario.objects.create(
            usuario=request.user,
            post=post,
            comentario=comentario_texto
        )
        messages.success(request, 'Comentário adicionado com sucesso.')

        # Redirecione para a página do post após o comentário ser salvo com sucesso
        return redirect('post-item', post_id=post_id)

def CurtirPost(request, post_id):
    # Se usuario não logado retorna para login
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')
    
    post = get_object_or_404(Post, pk=post_id) # Obtém o post com base no ID recebido ou retorna um erro 404 se não existir
    Curtida.objects.create(usuario=request.user, post=post)
    messages.success(request, 'Post curtido com sucesso')

    # Redireciona de volta para a página de onde veio
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
