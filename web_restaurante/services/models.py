from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre del Servicio")
    subtitle = models.CharField(max_length=200, verbose_name="Titulo",  null=True, blank=True)
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imágen", upload_to = 'services', null=True, blank=True)

    # Fecha de creación
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación") # Se ejecuta una sola vez, cuando se ha creado

    # Fecha de actualización
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización") # Se ejecuta cada vez que se actualiza el campo

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

        ordering = ['-created'] # Ordena de manera descendente

    def __str__(self):
        return self.title


