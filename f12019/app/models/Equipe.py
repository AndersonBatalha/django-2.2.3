from django.db import models
from .Cidade import Cidade

class Equipe(models.Model):
    nome_equipe = models.CharField(max_length=75, help_text="Nome da equipe")
    nome_oficial = models.CharField(max_length=130, help_text="Nome oficial da equipe")
    numero_titulos = models.IntegerField(help_text="Número de títulos")
    voltas_mais_rapidas = models.IntegerField(help_text="Quantidade de voltas mais rápidas")
    pole_positions = models.IntegerField(help_text="Quantidade de pole positions")
    unidade_potencia = models.CharField(max_length=35, help_text="Unidade de potência")
    chassi = models.CharField(max_length=20)
    primeiro_campeonato = models.IntegerField(help_text="Primeiro campeonato disputado")
    posicao_melhor_resultado = models.IntegerField(help_text="Melhor resultado conquistado")
    nr_melhor_resultado = models.IntegerField()
    url = models.URLField(help_text="URL")
    img = models.FileField(help_text="Imagem")
    logo = models.CharField(max_length=50)
    flag_icon = models.CharField(max_length=5)

    cidade = models.ForeignKey(Cidade, verbose_name="Sede da equipe", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_equipe

    class Meta:
        db_table = 'equipe'
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"