from django.db import models
from .Categoria import Categoria
from .Post import Post

class Categoria_Post(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)

    categorias = models.ManyToManyField(Categoria, verbose_name="categorias do post")

    def __str__(self):
        return self.post, '-', self.categorias

    class Meta:
        db_table = 'post_categoria'
        verbose_name = "Categoria do post"
        verbose_name_plural = "Categorias dos posts"
