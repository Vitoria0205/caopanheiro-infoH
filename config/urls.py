# config/urls.py (ou seu arquivo principal de URLs)
from django.contrib import admin
from django.urls import path
from app.views import IndexView, HistoriaView, LocalizacaoView, LoginView, cadastro_view  # <-- Importe a função!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('historia/', HistoriaView.as_view(), name='historia'),          # use / no final
    path('localizacao/', LocalizacaoView.as_view(), name='localizacao'), # use / no final
    path('login/', LoginView.as_view(), name='login'),                  # use / no final
    path('cadastro/', cadastro_view, name='cadastro'),                  # só uma rota!
]