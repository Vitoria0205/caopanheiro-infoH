# config/urls.py
from django.contrib import admin
from django.urls import path
from app.views import IndexView, HistoriaView, LocalizacaoView, cadastro_view, login_view  # ✅ Importe login_view, não LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('historia/', HistoriaView.as_view(), name='historia'),
    path('localizacao/', LocalizacaoView.as_view(), name='localizacao'),
    path('login/', login_view, name='login'),        # ✅ Use a função login_view
    path('cadastro/', cadastro_view, name='cadastro'),
]