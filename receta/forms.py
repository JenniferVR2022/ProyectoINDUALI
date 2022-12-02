from django.forms import ModelForm, widgets
from django_select2 import forms as s2forms
from ingrediente.models import Ingrediente
from receta.models import Receta,RecetaDetalle


class IngredienteWidget(s2forms.ModelSelect2Widget):
    search_fields ={
        "nombre__icontains",
        "id__icontains"
    }

class RecetaForm(ModelForm):
    class Meta:
        model= Receta
        exclude=['estado','super','estandar']
        widgets={
          'ingrediente':IngredienteWidget,
        }


class RecetaDetalleForm(ModelForm):
    class Meta:
        model= RecetaDetalle
        fields='__all__'
        widgets={
            'ingrediente':IngredienteWidget
        }
