from django.db import models

class Funcao(models.Model):
    funcao = models.CharField(max_length=50, unique=True, help_text="Função do usuário no sistema")
    permissao = models.IntegerField()

    def __str__(self):
        return self.funcao

    class Meta:
        db_table = 'role'
        verbose_name = "Função"
        verbose_name_plural = "Funções"