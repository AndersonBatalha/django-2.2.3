from django.db import models
from .Cidade import Cidade
from .Equipe import Equipe

class Piloto(models.Model):
    nome = models.CharField(max_length=125, help_text='Nome do piloto')
    slug = models.SlugField(max_length=100)
    numero = models.IntegerField()
    pontos_ganhos = models.IntegerField()
    data_nasc = models.DateField()
    corridas_disputadas = models.IntegerField()
    numero_podios = models.IntegerField()
    numero_titulos = models.IntegerField()
    pos_melhor_resultado = models.IntegerField()
    nr_melhor_resultado = models.IntegerField()
    img = models.FileField()
    flag_icon = models.CharField(max_length=5)

    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'piloto'
        verbose_name = "Piloto"
        verbose_name_plural = "Pilotos"