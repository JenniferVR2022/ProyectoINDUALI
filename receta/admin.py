from django.contrib import admin
from .models import Receta
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class RecetaResource(resources.ModelResource):
    class Meta:
        model = Receta

class RecetaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nomReceta']
    list_display = ('codReceta', 'nomReceta', 'display_ingredientes',)  # Utilizamos el método 'display_nomIngrediente'
    resource_class = RecetaResource

    def display_ingredientes(self, obj):
         return ", ".join([receta_ingrediente.ingrediente.nomIngrediente for receta_ingrediente in obj.recetaingrediente_set.all()])
    display_ingredientes.short_description = 'Nombre Ingrediente'
    
    
  


admin.site.register(Receta, RecetaAdmin)