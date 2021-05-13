from django.db import models
from ckeditor.fields import RichTextField


class Pedido(models.Model):
    fecha = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    correo = models.EmailField(verbose_name="Email")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    direccion = models.CharField(max_length=200, verbose_name="Calle y Número",
                                 help_text='<span class="font-italic" style="font-size: 0.9rem">Nombre de la calle y número</span>')
    colonia = models.CharField(max_length=200, verbose_name="Colonia o Fraccionamiento",
                               help_text='<span class="font-italic" style="font-size: 0.9rem">Nombre de la colonia o fraccionamiento</span>')
    total = models.DecimalField(verbose_name="Total", max_digits=8,  decimal_places=2,
                                help_text='<span class="text-danger" style="font-size: 0.9rem">Cantidad a pagar por su pedido</span>')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ["-fecha"]

    def __str__(self):
        return str(self.id)


class Recipe(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "receta"
        verbose_name_plural = "recetas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
