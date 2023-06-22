from django import forms
from .models import Receta, Ingrediente

class recetaForm(forms.ModelForm):
    cantidadMateriaPrima = forms.DecimalField(label="Cantidad de Materia Prima", decimal_places=2, min_value=0)
    ingredientes = forms.ModelMultipleChoiceField(
        queryset=Ingrediente.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Permite que el campo sea opcional
    )

    class Meta:
        model = Receta
        fields = ['nomComponente', 'codReceta', 'nomReceta', 'estado', 'estandar', 'preparacion', 'cantidadMateriaPrima', 'ingredientes']

    def save(self, commit=True):
        receta = super().save(commit=False)
        
        # Limpiar la relación ManyToMany existente
        receta.ingredientes.clear()

        # Guardar la receta para obtener un ID válido
        if commit:
            receta.save()

        # Agregar los ingredientes seleccionados a la receta
        for ingrediente in self.cleaned_data['ingredientes']:
            receta.ingredientes.add(ingrediente)

        return receta
