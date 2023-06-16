from django.contrib import admin
from .models import CentroCosto
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

class CentroCostoResource(resources.ModelResource):
    class Meta:
        model = CentroCosto

class CentroCostoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nomCentroCostos']
    list_display = ('codCentroCostos', 'nomCentroCostos',)
    resource_class = CentroCostoResource
    
admin.site.register(CentroCosto, CentroCostoAdmin)