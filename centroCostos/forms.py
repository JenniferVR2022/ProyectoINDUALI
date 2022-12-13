from django.forms import ModelForm
from centroCostos.models import  CentroCosto

class CentroCostoForm(ModelForm):
    class Meta:
        model= CentroCosto
        exclude=['estado']
        
