from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Columas que se quieren mostrar
    list_display = ('title', 'updated')
    ordering = ('title',)
    search_fields = ('title', )


admin.site.register(Recipe, RecipeAdmin)
