from django.db import models
from .Grupo import Grupo
from .Usuario import Usuario

class MembrosGrupo(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    membros = models.ManyToManyField(Usuario)

    def __str__(self):
        return "%s - %s" %(self.grupo.nome_grupo, self.membros.nome_usuario)

    class Meta:
        db_table = 'membros_grupo'
        verbose_name = "Participante do grupo"
        verbose_name_plural = "Participantes dos grupos"