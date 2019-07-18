from django.db import models
from .Usuario import Usuario
from .Post import Post

class Comentario(models.Model):
    texto = models.TextField(max_length=500, help_text="Comentário")
    data = models.DateTimeField(help_text="Data e hora do comentário")

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.autor.nome_usuario, self.post.titulo)

    class Meta:
        db_table = 'comentario'
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"