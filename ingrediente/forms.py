from django.forms import ModelForm
from ingrediente.models import Ingrediente

class IngredienteForm(ModelForm):
    class Meta:
          model= Ingrediente
          exclude=['estado']


