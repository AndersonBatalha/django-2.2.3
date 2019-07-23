from slugify import slugify

from django.db import models
from .Cidade import Cidade
from .Equipe import Equipe
from .Titulo import Titulo

class Piloto(models.Model):
    nome = models.CharField(max_length=125, help_text='Nome do piloto')
    slug = models.SlugField(max_length=100, editable=False)
    numero = models.IntegerField(blank=True)
    pontos_ganhos = models.IntegerField(blank=True)
    data_nasc = models.DateField()
    corridas_disputadas = models.IntegerField(blank=True)
    numero_podios = models.IntegerField(blank=True)
    numero_titulos = models.IntegerField(blank=True)
    pos_melhor_resultado = models.IntegerField(blank=True)
    nr_melhor_resultado = models.IntegerField(blank=True)
    img = models.FileField(blank=True)
    flag_icon = models.CharField(max_length=5)

    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    titulos = models.ManyToManyField(Titulo)

    def __init__(self, *args, **kwargs):
        super(Piloto, self).__init__(*args, **kwargs)
        if self.nome != None:
            self.slug = slugify(self.nome)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'piloto'
        verbose_name = "Piloto"
        verbose_name_plural = "Pilotos"