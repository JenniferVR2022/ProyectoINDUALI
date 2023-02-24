from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.

class Ingrediente (models.Model):
    codIngrediente=models.CharField(max_length=50, verbose_name="Codigo Ingrediente")
    nomIngrediente=models.CharField(max_length=50, verbose_name="Nombre Ingrediente")
    unidadMedida=models.CharField(max_length=50, verbose_name="Unidad de Medida")
    cantidadMateriaPrima=models.CharField(max_length=50, verbose_name="Cantidad Materia Prima")
    estado = models.BooleanField (default=True,verbose_name="Estado")

    def __str__(self):
        fila = "Nombre: "+ self.nomIngrediente + " - Unidad: " + self.unidadMedida 
        return fila