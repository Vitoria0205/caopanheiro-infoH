from django.contrib import admin
from django.urls import path
from app.views import IndexView, HistoriaView, LocalizacaoView, CadastroView, LoginView, cadastro_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('historia', HistoriaView.as_view(), name='historia'),
    path('localizacao.html', LocalizacaoView.as_view(), name='localizacao'),
    path('cadastro.html', CadastroView.as_view(), name='cadastro'),
    path('login.html', LoginView.as_view(), name='login'),
    path('cadastro/', cadastro_view, name='cadastro'),
]


