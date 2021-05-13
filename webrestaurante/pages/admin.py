from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Columas que se quieren mostrar
    list_display = ('title', 'updated')
    ordering = ('title',)
    search_fields = ('title', )


admin.site.register(Page, PageAdmin)
