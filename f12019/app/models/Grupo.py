from slugify import slugify

from django.db import models
from .Usuario import Usuario

class Grupo(models.Model):
    nome_grupo = models.CharField(max_length=75, help_text="Nome do grupo")
    slug = models.SlugField(max_length=150, help_text="Slug", editable=False)
    descricao = models.TextField(max_length=300, help_text="Descrição do grupo", blank=True)

    membros = models.ManyToManyField(Usuario)

    def __init__(self, *args, **kwargs):
        super(Grupo, self).__init__(*args, **kwargs)
        if self.nome_grupo != None:
            self.slug = slugify(self.nome_grupo)

    def __str__(self):
        return self.nome_grupo

    class Meta:
        db_table = 'grupo'
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"