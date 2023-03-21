from django.forms import ModelForm, widgets
from django_select2 import forms as s2forms
from receta.models import Receta
from django import forms

class IngredienteWidget(s2forms.ModelSelect2Widget):
    search_fields ={
        "nombre__icontains",
        "id__icontains"
    }

class recetaForm(ModelForm):
    class Meta:
        model= Receta
        exclude=['CodReceta']
        

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'
        widgets = {
            'estado': forms.Select(choices=Receta.Estado.choices, attrs={'class': 'form-select'})
        }        