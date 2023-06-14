from django.forms import ModelForm, widgets
from django_select2 import forms as s2forms
from receta.models import Receta


from django import forms

class MyForm(forms.Form):
    phone = forms.BooleanField(required=True)

class IngredienteWidget(s2forms.ModelSelect2Widget):
    search_fields ={
        "nombre__icontains",
        "id__icontains"
    }
        
  
class recetaForm(forms.ModelForm):
    cantidadMateriaPrima = forms.DecimalField(label="Cantidad de Materia Prima", decimal_places=2, min_value=0)
    
    class Meta:
        model = Receta
        fields = ['nomComponente', 'codReceta', 'nomReceta', 'estado', 'estandar', 'preparacion', 'nomIngrediente', 'cantidadMateriaPrima']      
