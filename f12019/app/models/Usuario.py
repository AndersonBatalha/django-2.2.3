from django.db import models
from .Funcao import Funcao
from django.core.validators import EmailValidator, URLValidator

class Usuario(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome completo")
    nome_usuario = models.CharField(max_length=75, help_text="Nome de usuário")
    email = models.EmailField(validators=[
        EmailValidator(message="Entre com um endereço de e-mail válido")
    ])
    data_nasc = models.DateField()
    endereco = models.CharField(max_length=300, help_text="Endereço", blank=True)
    complemento = models.CharField(max_length=150, help_text="Complemento", blank=True)
    bairro = models.CharField(max_length=100, help_text="Bairro", blank=True)
    cidade = models.CharField(max_length=100, help_text="Cidade", blank=True)
    estado = models.CharField(max_length=100, help_text="Estado", blank=True)
    pais = models.CharField(max_length=100, help_text="Estado", blank=True)
    hash_senha = models.CharField(max_length=100)
    avatar = models.URLField(max_length=125,
                             help_text="URL do Gravatar",
                             validators=[
                                 URLValidator(message="Informe uma URL válida")
                             ], blank=True)

    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_usuario

    class Meta:
        db_table = "usuario"
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"