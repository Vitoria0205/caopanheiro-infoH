# config/urls.py

from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView, HistoriaView, LocalizacaoView, HistoriaIndividualView,
    cadastro_view, login_view, logout_view, perfil, formulario_view,
    confirmacao_adocao_view, notificacao
)
from app.admin_shortcut import admin_shortcut, admin_info
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('historia/', HistoriaView.as_view(), name='historia'),  # Página única com todas as histórias
    path('localizacao/', LocalizacaoView.as_view(), name='localizacao'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('perfil/', perfil, name='perfil'),
    path('admin-info/', admin_info, name='admin_info'),
    path('admin-acesso/', admin_shortcut, name='admin_shortcut'),
    path('formulario/<int:animal_id>/', formulario_view, name='formulario'),
    path('confirmacao-adocao/<int:adocao_id>/', confirmacao_adocao_view, name='confirmacao_adocao'),
    path('notificacao/', notificacao, name='notificacao'),
    # Opcional: mantém a rota antiga (redireciona ou remove)
    # path('historia/<int:animal_id>/', HistoriaIndividualView.as_view(), name='historia_individual'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)