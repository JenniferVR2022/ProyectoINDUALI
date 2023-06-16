from django.contrib import admin
from .models import ListaPrecio
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

class ListaPrecioResource(resources.ModelResource):
    class Meta:
        model = ListaPrecio

class ListaPrecioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nomListaPrecio']
    list_display = ('codListaPrecio', 'nomListaPrecio', 'tipoLista',)
    resource_class = ListaPrecioResource
    
admin.site.register(ListaPrecio, ListaPrecioAdmin)