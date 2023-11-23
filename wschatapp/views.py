from django.shortcuts import render

def Login(request):
    return render(request, 'wschatapp/login.html')

def Cadastro(request):
    return render(request, 'wschatapp/cadastro.html')