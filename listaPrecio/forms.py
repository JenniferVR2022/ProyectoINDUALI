from dataclasses import field
from django.forms import ModelForm
from listaPrecio.models import ListaPrecio


class listaPForm(ModelForm):
    class Meta:
        model= ListaPrecio
        exclude=['estado']