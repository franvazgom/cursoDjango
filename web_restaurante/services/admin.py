from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    # Campos de lectura
    readonly_fields = ('created', 'updated')

# Register your models here.
admin.site.register(Service, ServiceAdmin)

