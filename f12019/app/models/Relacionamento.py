from django.db import models
from .Usuario import Usuario

class Relacionamento(models.Model):
    usuario = models.ForeignKey(Usuario, related_name="usuario", on_delete=models.DO_NOTHING)

    seguidor = models.ForeignKey(Usuario, related_name="seguidor", on_delete=models.DO_NOTHING)

    seguindo = models.BooleanField()

    def __init__(self, *args, **kwargs):
        super(Relacionamento, self).__init__(*args, **kwargs)
        self.seguindo = True

    def __str__(self):
        return "%s segue %s" % (self.usuario.nome_usuario, self.seguidor.nome_usuario)

    class Meta:
        db_table = 'relacionamento'
        verbose_name = "Relacionamento"
        verbose_name_plural = "Relacionamentos"