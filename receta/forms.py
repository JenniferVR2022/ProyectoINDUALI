from dataclasses import field
from django.forms import ModelForm
from receta.models import Receta


class RecetaForm(ModelForm):
    class Meta:
        model= Receta
        exclude=['estado']


