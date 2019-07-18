from django.db import models
from .Pontuacao import Pontuacao
from .Piloto import Piloto
from .Evento import Evento

class Resultado(models.Model):
    resultado = models.ForeignKey(Pontuacao, on_delete=models.DO_NOTHING)
    piloto = models.ForeignKey(Piloto, on_delete=models.DO_NOTHING)
    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING)

    melhor_volta = models.IntegerField(help_text="Melhor volta da corrida")

    def __str__(self):
        return self.evento, self.piloto, self.resultado

    class Meta:
        db_table = 'resultado'
        verbose_name = "Resultado"
        verbose_name_plural = "Resultados"