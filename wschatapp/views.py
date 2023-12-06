from itertools import chain
from django.db.models import Q
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from usuarios.forms import CadastroForms
from wschatapp.models import Comentario, Curtida, Post, Rede, UsuarioInfo, PostSalvo

def verificar_autenticacao(request): # Verificar se usuario está logado
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')


def variaveis_globais(request): # Variaveis Gerais
    global usuario, usuario_info, qtd_seguidos, qtd_seguidores, \
        posts, posts_salvos, posts_curtidos, usuarios_seguidos, \
        usuarios_seguidores, meus_posts, usuarios_cadastrados

    usuario = request.user # informações do usuario logado
    usuario_info = UsuarioInfo.objects.get(usuario=usuario) # Detalhes usuario
    lista_ids_seguidos = Rede.objects.filter(usuario=usuario).values_list('seguido', flat=True) # lista de ids seguidos
    lista_ids_seguidores = Rede.objects.filter(usuario=usuario).values_list('seguidor', flat=True) # lista de ids seguidores
    usuarios_seguidos = User.objects.filter(id__in=lista_ids_seguidos) # usuarios seguidos
    usuarios_seguidores = User.objects.filter(id__in=lista_ids_seguidores) # usuarios seguidores
    meus_posts = Post.objects.filter(usuario=usuario) # meus posts publicados
    outros_posts = Post.objects.filter(usuario__in=usuarios_seguidos)# postagens de quem sigo
    posts_salvos = PostSalvo.objects.filter(usuario=usuario).values_list('post__id', flat=True) # posts que eu salvei
    posts_curtidos = Curtida.objects.filter(usuario=usuario).values_list('post__id', flat=True) # posts que eu curti
    qtd_seguidos = Rede.objects.filter(usuario=usuario).exclude(seguido__isnull=True).count() # qtd de usuarios que sigo
    qtd_seguidores = Rede.objects.filter(usuario=usuario).exclude(seguidor__isnull=True).count() # qtd de usuarios que me seguem
    posts = sorted(list(chain(meus_posts, outros_posts)), key=lambda post: post.data_hora, reverse=True)# minhas postagens + de quem sigo
    for post in posts: # Add em posts: qtd de comentarios e curtidas 
        post.qtd_comentarios = Comentario.objects.filter(post=post).count()
        post.qtd_curtidas = Curtida.objects.filter(post=post).count()
    usuarios_cadastrados = UsuarioInfo.objects.all()


def PerfilPessoal(request):
    verificar_autenticacao(request)
    variaveis_globais(request)

    return render(request, 'wschatapp/perfil-pessoal.html', {
        'posts': posts,
        'usuario_info': usuario_info,
        'usuario': usuario,
        'posts_salvos': posts_salvos,
        'posts_curtidos': posts_curtidos,
        'qtd_seguidos': qtd_seguidos,
        'qtd_seguidores': qtd_seguidores,
    })


def PerfilUsuario(request, user_id):
    verificar_autenticacao(request)
    variaveis_globais(request)
    
    outro_usuario = get_object_or_404(User, pk=user_id)
    postsuser = Post.objects.filter(usuario=outro_usuario)
    usuario_info = UsuarioInfo.objects.get(usuario=outro_usuario)
    esta_seguindo = Rede.objects.filter(usuario=usuario, seguido=outro_usuario).exists() # Verifica se já estou seguindo o outro_usuario
    
    return render(request, 'wschatapp/perfil-usuario.html',{
        'postsuser': postsuser, 
        'usuario_info': usuario_info, 
        'outro_usuario': outro_usuario, 'esta_seguindo': esta_seguindo
    })


def SeguirUsuario(request, user_id):
    verificar_autenticacao(request)
    variaveis_globais(request)

    outro_usuario = get_object_or_404(User, pk=user_id) # usuario para seguir
    Rede.objects.create(usuario=usuario, seguido=outro_usuario) # salva outro_usuario como seguido
    
    return redirect('perfil-usuario', user_id=user_id)


def NaoSeguirUsuario(request, user_id):
    verificar_autenticacao(request)
    variaveis_globais(request)
    
    outro_usuario = get_object_or_404(User, pk=user_id) # usuario para não seguir
    Rede.objects.filter(usuario=usuario, seguido=outro_usuario).delete() # Deleta outro_usuario como seguido

    return redirect('perfil-usuario', user_id=user_id)


def Config(request):
    verificar_autenticacao(request)
    variaveis_globais(request)

    form = CadastroForms(request.POST or None, initial={ # Dados para preencher formulário no html
        'nome_usuario': usuario.username,
        'sobrenome': usuario.last_name,
        'email': usuario.email,
    })

    if request.method == 'POST':
        form = CadastroForms(request.POST, request.FILES) # informações do formulário html

        # Atualizando informações do usuario 
        if form.is_valid():
            usuario.username = form.cleaned_data['nome_usuario']
            usuario.last_name = form.cleaned_data['sobrenome']
            usuario.email = form.cleaned_data['email']
            nova_senha = form.cleaned_data['senha']
            
            if nova_senha: # se a senha for alterada, use set_password.
                usuario.set_password(nova_senha)
                usuario.save()
            else:
                usuario.save()
        
            foto_perfil = request.FILES.get('foto_perfil') # Atualizando foto do perfil
            if foto_perfil:
                usuario_info.foto_perfil = foto_perfil
                usuario_info.save()

            update_session_auth_hash(request, usuario) # Atualiza a sessão do usuário após a alteração de informações
            messages.success(request, 'Informações atualizadas com sucesso')
            return redirect('config')

    return render(request, 'wschatapp/config.html', {
        'usuario_info': usuario_info, 
        'form': form, 
        'usuario': usuario,
        'qtd_seguidos': qtd_seguidos,
        'qtd_seguidores': qtd_seguidores,
    })


def MinhaRede(request):
    verificar_autenticacao(request)
    variaveis_globais(request)

    return render(request, 'wschatapp/rede.html', {
        'usuarios_seguidos': usuarios_seguidos, 
        'usuarios_seguidores': usuarios_seguidores, 
        'usuario':usuario, 
        'usuario_info': usuario_info
    })


def PostItem(request, post_id):
    verificar_autenticacao(request)
    variaveis_globais(request)
    
    post = get_object_or_404(Post, pk=post_id) # post selecionado
    comentarios_post = Comentario.objects.filter(post_id=post_id).select_related('usuario__usuarioinfo') # usuarios e comentarios do post selecionado
    curtidas_post = Curtida.objects.filter(post_id=post_id).select_related('usuario__usuarioinfo') # usuarios que curtiram o post selecionado

    return render(request, 'wschatapp/post-item.html', 
        {'usuario_info': usuario_info,
         'post': post, 
         'posts_salvos': posts_salvos,
         'comentarios_post': comentarios_post,
         'curtidas_post': curtidas_post,
         'usuario': usuario})


def SalvarPost(request, post_id):
    verificar_autenticacao(request)
    variaveis_globais(request)

    post = Post.objects.get(id=post_id) # post selecionado
    PostSalvo.objects.create(usuario=request.user, post=post) # salva post selecionado

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def NaoSalvarPost(request, post_id):
    verificar_autenticacao(request)
    variaveis_globais(request)

    post = get_object_or_404(PostSalvo, usuario=request.user, post_id=post_id) # post selecionado
    post.delete() # Deleta o post

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def PostsSalvos(request):
    verificar_autenticacao(request)
    variaveis_globais(request)

    posts = Post.objects.filter(id__in=posts_salvos) # Obtém os detalhes dos posts salvos pelo usuário atual

    return render(request, 'wschatapp/posts-salvos.html', {
        'usuario': usuario ,
        'usuario_info': usuario_info, 
        'posts': posts
    })


def MeusPosts(request):
    verificar_autenticacao(request)
    variaveis_globais(request)
    
    return render(request, 'wschatapp/meus-posts.html', {
        'meus_posts': meus_posts, 
        'usuario_info': usuario_info, 
        'usuario': usuario
    })


def NovoPost(request):
    verificar_autenticacao(request)
    variaveis_globais(request)

    return render(request, 'wschatapp/novo-post.html')


def SalvarPostNovo(request):
    verificar_autenticacao(request)
    variaveis_globais(request)
    
    if request.method == 'POST':
        descricao = request.POST.get('descricao') # campo descrição form 
        imagem = request.FILES.get('imagem') # campo imagem form 

        novo_post = Post(usuario=request.user, descricao=descricao, imagem=imagem) # salva novo post
        novo_post.save()

        return redirect('perfil-pessoal')
    
    messages.error(request, 'Post não foi salvo')
    return render(request, 'wschatapp/novo-post.html')


def EditarPost(request, post_id):
    verificar_autenticacao(request)
    variaveis_globais(request)
    
    post = get_object_or_404(Post, pk=post_id) # post selecionado

    return render(request, 'wschatapp/editar-post.html', {'post': post})


def SalvarPostEditado(request, post_id):
    verificar_autenticacao(request)
    variaveis_globais(request)
    
    post = get_object_or_404(Post, pk=post_id) # post selecionado editado
    if request.method == 'POST':
        descricao = request.POST.get('descricao') # campo descrição form 
        imagem = request.FILES.get('imagem') # campo imagem form 
        
        if not descricao: # Verifique se a descrição está presente
            return HttpResponseBadRequest('A descrição não pode estar vazia.')
        
        post.descricao = descricao # edita campo descricao
        if imagem:
            if imagem.content_type.startswith('image'): # verifica se o arquivo é uma imagem
                post.imagem = imagem
            else:
                return HttpResponseBadRequest('O arquivo enviado não é uma imagem válida.')
        post.save()

        return redirect('perfil-pessoal')

    return render(request, 'wschatapp/perfil-pessoal.html')


def DeletarPost(request, post_id):
    verificar_autenticacao(request)
    variaveis_globais(request)
    
    post = get_object_or_404(Post, pk=post_id) # post selecionado
    post.delete()

    return redirect('perfil-pessoal')


def BuscarUsuarios(request):
    verificar_autenticacao(request)
    variaveis_globais(request)
    
    return render(request, 'wschatapp/buscar-usuarios.html', {
        'usuario_info': usuario_info,
        'usuario': usuario,
        'usuarios_cadastrados': usuarios_cadastrados
    })


def PesquisarUsuarios(request):
    verificar_autenticacao(request)
    variaveis_globais(request)
    
    if request.method == 'POST':
        texto_pesquisa = request.POST.get('texto-pesquisa') # valor para pesquisar usuarios

        if texto_pesquisa:
            # Pesquisa insensível a maiúsculas e minúsculas, e filtra usuarios correspondentes
            usuarios_cadastrados = UsuarioInfo.objects.filter( Q(usuario__username__icontains=texto_pesquisa) )
        else:
            usuarios_cadastrados = UsuarioInfo.objects.all()
    else:
        usuarios_cadastrados = UsuarioInfo.objects.all()

    return render(request, 'wschatapp/buscar-usuarios.html', {'usuarios_cadastrados': usuarios_cadastrados})


def ComentarPost(request, post_id):
    verificar_autenticacao(request)
    variaveis_globais(request)
    
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id) # post selecionado

        comentario_texto = request.POST.get('comentario') # campo comentario form 

        if not comentario_texto:
            messages.error(request, 'O campo de comentário está vazio.')
            return redirect('perfil-pessoal')

        novo_comentario = Comentario.objects.create( # salva um novo comentario
            usuario=usuario,
            post=post,
            comentario=comentario_texto
        )
        messages.success(request, 'Comentário adicionado com sucesso.')

        return redirect('post-item', post_id=post_id)


def DeletarComentario(request, comentario_id):
    verificar_autenticacao(request)
    variaveis_globais(request)
    
    comentario = get_object_or_404(Comentario, pk=comentario_id) # comentario selecionado
    comentario.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def CurtirPost(request, post_id):
    verificar_autenticacao(request)
    variaveis_globais(request)
    
    post = get_object_or_404(Post, pk=post_id) # post selecionado
    Curtida.objects.create(usuario=request.user, post=post) # salva curtida para post selecionado
    messages.success(request, 'Post curtido com sucesso')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def NaoCurtir(request, post_id):
    verificar_autenticacao(request)
    variaveis_globais(request)

    post_curtido = get_object_or_404(Curtida, post_id=post_id, usuario=request.user) # post selecionado
    post_curtido.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))