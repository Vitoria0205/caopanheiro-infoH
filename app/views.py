# app/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import CadastroPessoaForm  # <-- Importante!
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class HistoriaView(View):
    def get(self, request):
        return render(request, 'historia.html')


class LocalizacaoView(View):
    def get(self, request):
        return render(request, 'localizacao.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # Implementação futura
        return redirect('index')


# Função para cadastro (com formulário Django)
def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroPessoaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('login')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = CadastroPessoaForm()

    return render(request, 'cadastro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo de volta, {user.username}!')
                return redirect('perfil')  # ou 'index'
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})