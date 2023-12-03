from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from wschatapp.models import UsuarioInfo


# Create your views here.
def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST': #Se o método de envio é POST
        form = CadastroForms(request.POST, request.FILES) # Requisições POST e arquivos

        if form.is_valid(): # Se os campos são válidos
            form_cleaned = form.cleaned_data
            if form_cleaned['senha'] != form_cleaned['senha_check']: # Se as senhas não coincidem
                return redirect('cadastro') # Redireciona para a rota cadastro
            
            nome_usuario = form_cleaned['nome_usuario']
            sobrenome = form_cleaned['sobrenome']
            email = form_cleaned['email']
            senha = form_cleaned['senha']

            if User.objects.filter(username=nome_usuario).exists(): # Se o usuário já existe
                return redirect('cadastro') # Redireciona para a rota cadastro

            # Salvar novo usuário na tabela User
            usuario = User.objects.create_user(
                username=nome_usuario,
                last_name=sobrenome,
                email=email,
                password=senha
            )

            # Salvar a imagem de perfil na tabela UsuarioInfo
            if 'foto_perfil' in request.FILES:
                foto_perfil = request.FILES['foto_perfil']
                usuario_info = UsuarioInfo.objects.create(usuario=usuario, foto_perfil=foto_perfil)
                usuario_info.save() # Salva alterações na tabela UsuarioInfo

            return redirect('login') # Redireciona para a rota login
        
    return render(request, 'usuarios/cadastro.html', {'form': form})