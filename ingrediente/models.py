from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.

class Ingrediente (models.Model):
    codIngrediente=models.CharField(max_length=50, verbose_name="Cod Ingrediente")
    nomIngrediente=models.CharField(max_length=50, verbose_name="Nom Ingrediente")
    unidadMedida=models.CharField(max_length=50, verbose_name="Unidad Medida")
    cantidadMateriaPrima=models.CharField(max_length=50, verbose_name="Cantidad Materia Prima")
    