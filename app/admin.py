# app/admin.py
from django.contrib import admin
from .models import Pessoa, Cidade, Caracteristica, Animal, Formulario, Adocao, Doacao, Historia

# Registre todos os modelos para aparecerem no admin
admin.site.register(Pessoa)
admin.site.register(Cidade)
admin.site.register(Caracteristica)
admin.site.register(Animal)
admin.site.register(Formulario)
admin.site.register(Adocao)
admin.site.register(Doacao)
admin.site.register(Historia)