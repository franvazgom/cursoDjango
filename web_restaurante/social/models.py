from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red Social", max_length=200)
    url = models.URLField(verbose_name="Link", max_length=200, null=True, blank=True)
    # Fecha de creación
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación") # Se ejecuta una sola vez, cuando se ha creado

    # Fecha de actualización
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización") # Se ejecuta cada vez que se actualiza el campo

    class Meta:
        verbose_name="Link"
        verbose_name_plural = "Links"
        ordering = ['name']

    def __str__(self):
        return self.name