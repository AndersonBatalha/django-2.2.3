from django.db import models

class Titulo(models.Model):
    ano_titulo = models.IntegerField(help_text="Ano do título")

    def __str__(self):
        return "%d" %(self.ano_titulo)

    class Meta:
        db_table = "titulo"
        verbose_name = "Título mundial"
        verbose_name_plural = "Títulos mundiais"