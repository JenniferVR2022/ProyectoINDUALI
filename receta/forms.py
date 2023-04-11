from django.forms import ModelForm, widgets
from django_select2 import forms as s2forms
from receta.models import Receta
from django import forms

class IngredienteWidget(s2forms.ModelSelect2Widget):
    search_fields ={
        "nombre__icontains",
        "id__icontains"
    }


class RecetaForm(forms.ModelForm):
    estado = forms.ChoiceField(choices=Receta.Estado.choices)
    
    class Meta:
        model = Receta
        fields = ['codReceta', 'nomReceta', 'estado', 'estandar', 'preparacion', 'codComponente', 'ingrediente']



class recetaForm(ModelForm):
    class Meta:
        model= Receta
        exclude=['CodReceta']