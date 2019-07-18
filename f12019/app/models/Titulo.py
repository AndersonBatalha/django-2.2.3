from django.db import models
from .Piloto import Piloto

class Titulo(models.Model):
    ano_titulo = models.IntegerField(help_text="Ano do título")

    piloto = models.ForeignKey(Piloto, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s (%d)" %(self.piloto.nome, self.ano_titulo)

    class Meta:
        db_table = "titulo"
        verbose_name = "Título mundial"
        verbose_name_plural = "Títulos mundiais"