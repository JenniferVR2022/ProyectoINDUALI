from django.contrib import admin
from .models import Ingrediente
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

class IngredienteResource(resources.ModelResource):
    class Meta:
        model = Ingrediente

class IngredienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nomIngrediente']
    list_display = ('codIngrediente', 'nomIngrediente', 'unidadMedida','costoIngrediente','estado')
    resource_class = IngredienteResource
    
    
    
admin.site.register(Ingrediente, IngredienteAdmin)

