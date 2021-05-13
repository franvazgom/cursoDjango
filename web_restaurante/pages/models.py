from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")

    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    
    # Fecha de creación
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación") # Se ejecuta una sola vez, cuando se ha creado

    # Fecha de actualización
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización") # Se ejecuta cada vez que se actualiza el campo

    class Meta:
        verbose_name="Página"
        verbose_name_plural = "Páginas"
        ordering = ['order','title']

    def __str__(self):
        return self.title