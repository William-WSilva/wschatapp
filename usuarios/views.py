import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages # biblioteca para autenticacao e mensagens
from usuarios.forms import LoginForms, CadastroForms
from wschatapp.models import UsuarioInfo

def login(request):
    form = LoginForms()

    if request.method == 'POST': # Se o método de envio é POST
        form = LoginForms(request.POST) # Requisições POST
        
        if form.is_valid(): # Se os campos são válidos
            nome=form['nome_login'].value()
            senha=form['senha'].value()

            # recurso django para autenticar informações (valido ou none)
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            # Se o usuario for valido executa autenticação login (auth)
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso')
                return redirect('perfil-pessoal')
            else:
                messages.error(request, 'Erro ao efetuar login')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST': #Se o método de envio é POST
        form = CadastroForms(request.POST, request.FILES) # Requisições POST e arquivos

        if form.is_valid(): # Se os campos são válidos
            form_cleaned = form.cleaned_data
            nome_usuario = form_cleaned['nome_usuario']
            sobrenome = form_cleaned['sobrenome']
            email = form_cleaned['email']
            senha = form_cleaned['senha']

            if User.objects.filter(username=nome_usuario).exists(): # Se o usuário já existe
                messages.error(request, 'Usuario já cadastrado')
                return redirect('cadastro') # Redireciona para a rota cadastro

            # Salvar novo usuário na tabela User
            usuario = User.objects.create_user(
                username=nome_usuario,
                last_name=sobrenome,
                email=email,
                password=senha
            )
            usuario.save()

            # Salvar a imagem de perfil na tabela UsuarioInfo
            foto_perfil = request.FILES.get('foto_perfil')
            if foto_perfil:
                usuario_info = UsuarioInfo.objects.create(usuario=usuario, foto_perfil=foto_perfil)
            else:
                caminho_imagem_padrao = 'imagem/foto_padrao.jpg'
                usuario_info = UsuarioInfo.objects.create(usuario=usuario, foto_perfil=caminho_imagem_padrao)
            usuario_info.save()  # Salva alterações na tabela UsuarioInfo

            messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('login') # Redireciona para a rota login
        
    return render(request, 'usuarios/cadastro.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso')
    return redirect('login')