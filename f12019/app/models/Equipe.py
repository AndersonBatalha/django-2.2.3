from django.db import models
from .Cidade import Cidade

class Equipe(models.Model):
    nome_equipe = models.CharField(max_length=75, help_text="Nome da equipe")
    nome_oficial = models.CharField(max_length=130, help_text="Nome oficial da equipe", blank=True)
    numero_titulos = models.IntegerField(help_text="Número de títulos", blank=True)
    voltas_mais_rapidas = models.IntegerField(help_text="Quantidade de voltas mais rápidas", blank=True)
    pole_positions = models.IntegerField(help_text="Quantidade de pole positions", blank=True)
    unidade_potencia = models.CharField(max_length=35, help_text="Unidade de potência", blank=True)
    chassi = models.CharField(max_length=20, blank=True)
    primeiro_campeonato = models.IntegerField(help_text="Primeiro campeonato disputado", blank=True)
    posicao_melhor_resultado = models.IntegerField(help_text="Melhor resultado conquistado", blank=True)
    nr_melhor_resultado = models.IntegerField(blank=True)
    url = models.URLField(help_text="URL", blank=True)
    img = models.FileField(help_text="Imagem", blank=True)
    logo = models.CharField(max_length=50, blank=True)
    flag_icon = models.CharField(max_length=5)

    cidade = models.ForeignKey(Cidade, verbose_name="Sede da equipe", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_equipe

    class Meta:
        db_table = 'equipe'
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"