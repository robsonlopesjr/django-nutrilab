from django.shortcuts import render, redirect
from django.http import HttpResponse

from .utils import password_is_valid


# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro')

        return HttpResponse(f'O usuario {usuario} tem o email {email}')


def logar(request):
    return HttpResponse('Você está na página de login')
