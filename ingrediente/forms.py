from dataclasses import field
from django.forms import ModelForm
from ingrediente.models import ingrediente


class IngredienteForm(ModelForm):
    class Meta:
        model= ingrediente
        exclude=['estado']