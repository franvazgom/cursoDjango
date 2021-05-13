from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    # redifinir los campos que son solo de lectura
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)
