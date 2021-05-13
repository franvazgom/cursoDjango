from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imágen", upload_to="projects")
    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web")

    # auto_now_add solo se ejecuta una sola vez.
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de cración")

    # auto_now se ejecuta cada vez que se modifica
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

        # Ordenación por defecto
        ordering = ['-created']

    # Para que nos regrese el nombre del proyecto en lugar de object
    def __str__(self):
        return self.title
