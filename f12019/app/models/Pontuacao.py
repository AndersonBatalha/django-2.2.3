from django.db import models

class Pontuacao(models.Model):
    posicao = models.IntegerField(help_text="Posição na corrida")
    pontuacao_corrida = models.IntegerField(help_text="Pontuação")

    def __str__(self):
        return "%dº = %d pontos" % (self.posicao, self.pontuacao_corrida)

    class Meta:
        db_table = 'pontuacao'
        verbose_name = "Pontuação"
        verbose_name_plural = "Pontuações"