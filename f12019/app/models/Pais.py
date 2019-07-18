from django.db import models

class Pais(models.Model):
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.pais

    class Meta:
        db_table = 'pais'
        verbose_name = "País"
        verbose_name_plural = "Países"