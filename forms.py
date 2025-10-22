# app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class CadastroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
        label="E-mail"
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome completo'}),
        label="Nome Completo"
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu sobrenome'}),
        label="Sobrenome"
    )
    idade = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '18', 'placeholder': 'Ex: 25'}),
        label="Idade"
    )
    telefone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
        label="Telefone"
    )
    endereco = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Rua, número, bairro...'}),
        required=False,
        label="Endereço"
    )
    cidade = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: São Paulo'}),
        label="Cidade"
    )
    newsletter = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label="Quero receber newsletter com novidades sobre adoções"
    )
    termos_aceitos = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='Aceito os <a href="#" target="_blank">termos e condições</a> e a <a href="#" target="_blank">política de privacidade</a>'
    )

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'idade', 'telefone', 'endereco', 'cidade', 'newsletter', 'password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mínimo 8 caracteres'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']  # sincroniza username = email
        if commit:
            user.save()
        return user