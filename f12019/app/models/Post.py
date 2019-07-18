from django.db import models
from .Usuario import Usuario

class Post(models.Model):
    titulo = models.CharField(max_length=100, help_text="Título do post")
    texto = models.TextField(max_length=500, help_text="Conteúdo do post")
    imagem = models.FileField(help_text="Imagem")
    slug = models.SlugField(help_text="Slug", max_length=50)
    data = models.DateTimeField(help_text="Data e hora da postagem")

    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'post'
        verbose_name = "Post"
        verbose_name_plural = "Posts"