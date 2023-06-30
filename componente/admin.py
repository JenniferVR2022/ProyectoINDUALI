from django.contrib import admin
from .models import Componente
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

class ComponenteResource(resources.ModelResource):
    class Meta:
        model = Componente

class ComponenteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nomComponente']
    list_display = ('codComponente', 'nomComponente')
    resource_class = ComponenteResource
    
    
admin.site.register(Componente, ComponenteAdmin)
