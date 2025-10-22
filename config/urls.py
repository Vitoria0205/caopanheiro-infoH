# config/urls.py
from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView, HistoriaView, LocalizacaoView,
    cadastro_view, login_view, logout_view, PerfilView
)
from app.admin_shortcut import admin_shortcut, admin_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('historia/', HistoriaView.as_view(), name='historia'),
    path('localizacao/', LocalizacaoView.as_view(), name='localizacao'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # ✅ Adicionado
    path('cadastro/', cadastro_view, name='cadastro'),
    path('perfil/', PerfilView.as_view(), name='perfil'),  # ✅ Adicionada rota de perfil
    # 🚀 Atalhos de admin (opcional)
    path('admin-info/', admin_info, name='admin_info'),
    path('admin-acesso/', admin_shortcut, name='admin_shortcut'),
]