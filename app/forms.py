# app/forms.py
from django import forms
from django.contrib.auth.hashers import make_password
from .models import Pessoa, Usuario

class CadastroPessoaForm(forms.ModelForm):
    confirmar_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirmar Senha"
    )
    termos_aceitos = forms.BooleanField(
        required=True,
        label='Aceito os <a href="#" target="_blank">termos e condições</a> e a <a href="#" target="_blank">política de privacidade</a>',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    newsletter = forms.BooleanField(
        required=False,
        label='Quero receber newsletter com novidades sobre adoções',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Pessoa
        fields = ['nome', 'idade', 'email', 'telefone', 'endereco', 'cidade', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome completo'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control', 'min': '18', 'placeholder': 'Ex: 25'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Rua, número, bairro...'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: São Paulo'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mínimo 6 caracteres'}),
        }
        labels = {
            'nome': 'Nome Completo',
            'idade': 'Idade',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'endereco': 'Endereço',
            'cidade': 'Cidade',
            'senha': 'Senha',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Pessoa.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")
        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")
        if senha and len(senha) < 6:
            raise forms.ValidationError("A senha deve ter pelo menos 6 caracteres.")
        return cleaned_data

    def save(self, commit=True):
        pessoa = super().save(commit=False)
        pessoa.senha = make_password(self.cleaned_data["senha"])
        if commit:
            pessoa.save()
        return pessoa
    


class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    idade = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '18'}))
    telefone = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}), required=False)
    cidade = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    newsletter = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    termos_aceitos = forms.BooleanField(
        required=True,
        label='Aceito os <a href="#" target="_blank">termos e condições</a> e a <a href="#" target="_blank">política de privacidade</a>',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'idade', 'telefone', 'endereco', 'cidade', 'newsletter', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'Nome de usuário',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.idade = self.cleaned_data.get('idade')
        user.telefone = self.cleaned_data.get('telefone')
        user.endereco = self.cleaned_data.get('endereco')
        user.cidade = self.cleaned_data.get('cidade')
        user.newsletter = self.cleaned_data.get('newsletter', False)
        if commit:
            user.save()
        return user