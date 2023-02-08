from django.forms import ModelForm, widgets
from django_select2 import forms as s2forms
from receta.models import Receta


class IngredienteWidget(s2forms.ModelSelect2Widget):
    search_fields ={
        "nombre__icontains",
        "id__icontains"
    }






class recetaForm(ModelForm):
    class Meta:
        model= Receta
        exclude=['CodReceta']