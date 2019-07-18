from django.db import models
from .Cidade import Cidade

class Circuito(models.Model):
    nome = models.CharField(max_length= 125, help_text="Nome do circuito")
    percurso = models.IntegerField(help_text="Percurso")
    numero_voltas = models.IntegerField(help_text="Número de voltas")
    distancia_total = models.IntegerField()
    primeira_corrida = models.IntegerField()
    piloto_recorde_pista = models.CharField(max_length=100)
    ano_recorde_pista = models.IntegerField()
    tempo_recorde_pista = models.TimeField()

    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.nome

    class Meta:
        db_table = 'circuito'
        verbose_name = "Circuito"
        verbose_name_plural = "Circuitos"