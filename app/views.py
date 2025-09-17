from django.shortcuts import render,redirect
from .models import *
from django.views import View
from .forms import RegistrationForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class HistoriaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'historia.html')
    class LocalizacaoView(View):
        def get(self, request, *args, **kwargs):
            return render(request, 'locais.html')

class LocalizacaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'localizacao.html')

class CadastroView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cadastro.html')

    def post(self, request, *args, **kwargs):
        # Aqui você pode pegar os dados enviados pelo formulário
        # Exemplo: nome = request.POST.get('nome')
        # Depois, salvar no banco se quiser
        return redirect('login')  # redireciona para a página de login após cadastro


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        # Aqui você pode verificar usuário e senha do formulário
        # Exemplo:
        # usuario = request.POST.get('usuario')
        # senha = request.POST.get('senha')
        # Se for válido:
        return redirect('index')  # redireciona para a página inicial após login
        # Se for inválido: return render(request, 'login.html', {'erro': 'Credenciais inválidas'})


def cadastro_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # redireciona para a home
    else:
        form = RegistrationForm()
    return render(request, 'cadastro.html', {'form': form})