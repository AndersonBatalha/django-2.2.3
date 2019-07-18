from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=80, help_text="Categoria do post")

    def __str__(self):
        return self.categoria

    class Meta:
        db_table = 'categoria'
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"