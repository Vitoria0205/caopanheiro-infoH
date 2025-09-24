# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome} - {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


# app/models.py
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da pessoa")
    idade = models.PositiveIntegerField(verbose_name="Idade")
    email = models.EmailField(unique=True, verbose_name="Email")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    endereco = models.TextField(verbose_name="Endereço")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")  # <-- ALTERADO: agora é CharField
    senha = models.CharField(max_length=128, verbose_name="Senha")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class Caracteristica(models.Model):
    PORTE_CHOICES = [
        ('pequeno', 'Pequeno'),
        ('medio', 'Médio'),
        ('grande', 'Grande'),
    ]
    IDADE_CHOICES = [
        ('filhote', 'Filhote'),
        ('jovem', 'Jovem'),
        ('adulto', 'Adulto'),
        ('idoso', 'Idoso'),
    ]
    TEMPERAMENTO_CHOICES = [
        ('calmo', 'Calmo'),
        ('ativo', 'Ativo'),
        ('tímido', 'Tímido'),
        ('brincalhão', 'Brincalhão'),
    ]

    idade = models.CharField(max_length=10, choices=IDADE_CHOICES, verbose_name="Faixa etária")
    raca = models.CharField(max_length=50, verbose_name="Raça")
    porte = models.CharField(max_length=10, choices=PORTE_CHOICES, verbose_name="Porte")
    temperamento = models.CharField(max_length=20, choices=TEMPERAMENTO_CHOICES, verbose_name="Temperamento")

    def __str__(self):
        return f"{self.raca} - {self.porte} ({self.idade})"

    class Meta:
        verbose_name = "Característica"
        verbose_name_plural = "Características"


class Animal(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do animal")
    imagem = models.ImageField(upload_to='animais/', verbose_name="Imagem do animal")
    caracteristica = models.OneToOneField(Caracteristica, on_delete=models.CASCADE, verbose_name="Características")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"


class Formulario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do solicitante")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Animal")
    motivo_adocao = models.TextField(verbose_name="Motivo para adoção")
    disponibilidade = models.TextField(verbose_name="Disponibilidade (tempo, espaço etc.)")
    data_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da solicitação")

    def __str__(self):
        return f"Formulário - {self.nome} para {self.animal.nome}"

    class Meta:
        verbose_name = "Formulário de Adoção"
        verbose_name_plural = "Formulários de Adoção"


class Adocao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Animal adotado")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Adotante")
    formulario = models.OneToOneField(Formulario, on_delete=models.CASCADE, verbose_name="Formulário vinculado")
    confirmacao = models.BooleanField(default=False, verbose_name="Confirmação da adoção")
    data_adocao = models.DateField(auto_now_add=True, verbose_name="Data da adoção")

    def __str__(self):
        status = "Confirmada" if self.confirmacao else "Pendente"
        return f"{self.animal.nome} - {self.pessoa.nome} ({status})"

    class Meta:
        verbose_name = "Adoção"
        verbose_name_plural = "Adoções"


class Doacao(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('pix', 'PIX'),
        ('cartao', 'Cartão'),
        ('dinheiro', 'Dinheiro'),
        ('transferencia', 'Transferência'),
    ]

    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor da doação")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data da doação")
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO_CHOICES, verbose_name="Forma de pagamento")
    nome_doador = models.CharField(max_length=100, verbose_name="Nome do doador", blank=True, null=True)

    def __str__(self):
        return f"Doação de R${self.valor} - {self.nome_doador or 'Anônimo'}"

    class Meta:
        verbose_name = "Doação"
        verbose_name_plural = "Doações"


class Historia(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título da história")
    descricao = models.TextField(verbose_name="Descrição da história")
    envolvidos = models.TextField(verbose_name="Envolvidos no projeto", blank=True, null=True)
    adocao = models.ForeignKey(Adocao, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Adoção relacionada")
    animais = models.ManyToManyField(Animal, verbose_name="Animais envolvidos", blank=True)
    data_atualizacao = models.DateField(auto_now=True, verbose_name="Data de atualização")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "História"
        verbose_name_plural = "Histórias"


class Usuario(AbstractUser):
    # Campos extras além do User padrão
    idade = models.PositiveIntegerField(null=True, blank=True, verbose_name="Idade")
    telefone = models.CharField(max_length=15, blank=True, verbose_name="Telefone")
    endereco = models.TextField(blank=True, verbose_name="Endereço")
    cidade = models.CharField(max_length=100, blank=True, verbose_name="Cidade")
    newsletter = models.BooleanField(default=False, verbose_name="Newsletter")

    # O Django já tem: username, email, first_name, last_name, password, etc.
    # Vamos usar email como login principal
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # ou remova se quiser só email

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
