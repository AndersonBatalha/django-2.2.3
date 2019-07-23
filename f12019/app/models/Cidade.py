from django.db import models
from .Pais import Pais

class Cidade(models.Model):
    cidade = models.CharField(max_length=150)

    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.cidade

    class Meta:
        db_table = 'cidade'
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"