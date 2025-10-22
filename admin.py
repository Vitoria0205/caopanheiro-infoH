# app/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    Usuario, Cidade, Caracteristica,
    Animal, Formulario, Adocao, Doacao, Historia
)

@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {
            'fields': ('first_name', 'last_name', 'username', 'idade', 'telefone', 'endereco', 'cidade', 'newsletter')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name',
                'password1', 'password2',
                'idade', 'telefone', 'endereco', 'cidade', 'newsletter',
                'is_active', 'is_staff', 'is_superuser'
            ),
        }),
    )

# Registra os demais modelos
admin.site.register(Cidade)
admin.site.register(Caracteristica)
admin.site.register(Animal)
admin.site.register(Formulario)
admin.site.register(Adocao)
admin.site.register(Doacao)
admin.site.register(Historia)