from django.db import models

class Grupo(models.Model):
    nome_grupo = models.CharField(max_length=75, help_text="Nome do grupo")
    slug = models.SlugField(max_length=150, help_text="Slug")
    descricao = models.TextField(max_length=300, help_text="Descrição do grupo")

    def __str__(self):
        return self.nome_grupo

    class Meta:
        db_table = 'grupo'
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"