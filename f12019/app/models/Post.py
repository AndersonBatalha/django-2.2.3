from slugify import slugify

from django.db import models
from .Usuario import Usuario
from .Categoria import Categoria

class Post(models.Model):
    titulo = models.CharField(max_length=100, help_text="Título do post")
    texto = models.TextField(max_length=500, help_text="Conteúdo do post")
    imagem = models.FileField(help_text="Imagem", blank=True)
    slug = models.SlugField(help_text="Slug", max_length=50, editable=False)
    data = models.DateTimeField(help_text="Data e hora da postagem", blank=True)

    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    categorias = models.ManyToManyField(Categoria, verbose_name="categorias do post")

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        if self.titulo != None:
            self.slug = slugify(self.titulo)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'post'
        verbose_name = "Post"
        verbose_name_plural = "Posts"