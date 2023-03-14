from django.db import models
from unittest.util import _MAX_LENGTH
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from receta.models import Receta
from ingrediente.models import Ingrediente
from listaPrecio.models import ListaPrecio
from centroCostos.models import CentroCosto


class Estandarizador (models.Model):
    idEstandarizador=models.CharField(max_length=50, verbose_name="id Estandarizador")
    porcionesEstandar=models.CharField(max_length=50, verbose_name="Porciones Estandar")
    codCentroCostos=models.ForeignKey(CentroCosto, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Cod Centro Costos")
    codReceta=models.ForeignKey(Receta, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Cod Receta")
    codListaPrecio=models.ForeignKey(ListaPrecio, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Cod Lista Precio")
    codIngrediente=models.ForeignKey(Ingrediente, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Cod Ingrediente")  
    

class ListaCentroCosto(models.Model):
    nomCentroCostos = models.CharField(max_length=100)
    CentroCosto = models.ForeignKey(CentroCosto, on_delete=models.CASCADE)
