from django.forms import ModelForm, widgets
from receta.models import Receta,RecetaDetalle
from django import forms
from django_select2 import forms as s2forms


class IngredientesWidget(s2forms.ModelSelect2Widget):
    search_fields ={
        "nombre__icontains",
        "id__icontains"
    }

class RecetaForm(ModelForm):
    class Meta:
        model= Receta
        exclude=['estado','super','estandar']
        widgets={
           forms.TextInput(
                attrs= {
                    'placeholder':'nomReceta'
                }
            )
        
        }



