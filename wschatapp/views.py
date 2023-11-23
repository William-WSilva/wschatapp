from django.shortcuts import render

def Login(request):
    return render(request, 'wschatapp/login.html')

def Cadastro(request):
    return render(request, 'wschatapp/cadastro.html')

def PerfilPessoal(request):
    return render(request, 'wschatapp/perfil-pessoal.html')

def PerfilUsuario(request):
    return render(request, 'wschatapp/perfil-usuario.html')

def Config(request):
    return render(request, 'wschatapp/config.html')

def Rede(request):
    return render(request, 'wschatapp/rede.html')

def PostSalvo(request):
    return render(request, 'wschatapp/post-salvo.html')

def MeuPost(request):
    return render(request, 'wschatapp/meu-post.html')

def NovoPost(request):
    return render(request, 'wschatapp/novo-post.html')