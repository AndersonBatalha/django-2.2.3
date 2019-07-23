from django.db import models
from .Circuito import Circuito

class Evento(models.Model):
    nome_evento = models.CharField(max_length=200, help_text="Nome do evento")
    local = models.CharField(max_length=80, help_text='Local do evento')
    data_inicio = models.DateField(help_text='Início do evento')
    data_termino = models.DateField(help_text='Fim do evento')
    url = models.URLField(help_text='URL', blank=True)
    img_evento = models.FileField(blank=True)
    flag_icon = models.CharField(max_length=5)

    circuito = models.ForeignKey(Circuito, verbose_name="Circuito onde se realiza o evento",
                                 on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.nome_evento

    class Meta:
        db_table = 'evento'
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
