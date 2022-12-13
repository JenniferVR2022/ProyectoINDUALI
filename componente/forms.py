from dataclasses import field
from django.forms import ModelForm
from componente.models import Componente


class ComponenteForm(ModelForm):
    class Meta:
        model= Componente
        exclude=['CodComponente']