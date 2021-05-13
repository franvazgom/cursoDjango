from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")

    # Fecha de creación
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación") # Se ejecuta una sola vez, cuando se ha creado

    # Fecha de actualización
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización") # Se ejecuta cada vez que se actualiza el campo

    class Meta:
        verbose_name = "Categoría" # Modifica nombre
        verbose_name_plural = "Categorías" # Modifica nombre
        ordering =['-created'] #Ordenar publicaciones primero el ultimo creado

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de Publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    autor = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    # Fecha de creación
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación") # Se ejecuta una sola vez, cuando se ha creado

    # Fecha de actualización
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización") # Se ejecuta cada vez que se actualiza el campo

    class Meta:
        verbose_name="Post"
        verbose_name_plural = "Posts"
        ordering = ['-created']

    def __str__(self):
        return self.title
