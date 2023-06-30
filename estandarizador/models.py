from django.db import models
from unittest.util import _MAX_LENGTH
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from receta.models import Receta
from ingrediente.models import Ingrediente
from listaPrecio.models import ListaPrecio
from centroCostos.models import CentroCosto


class Estandarizador(models.Model):
    idEstandarizador = models.CharField(max_length=50, verbose_name="id Estandarizador")
    porcionesEstandar = models.CharField(max_length=50, verbose_name="Porciones Estandar")
    nomListaPrecio = models.CharField(max_length=50, verbose_name="Nombre Lista Precio", null=True, blank=True, editable=False)
    nomCentroCostos = models.CharField(max_length=50, verbose_name="Nombre Centro Costos", null=True, blank=True, editable=False)
    nomReceta = models.CharField(max_length=50, verbose_name="Nombre Receta", null=True, blank=True, editable=False)

    def __str__(self):
        return self.idEstandarizador

    def save(self, *args, **kwargs):
        if self.codListaPrecio:
            self.nomListaPrecio = self.codListaPrecio.nomListaPrecio
        if self.codCentroCostos:
            self.nomCentroCostos = self.codCentroCostos.nomCentroCostos
        if self.codReceta:
            self.nomReceta = self.codReceta.nomReceta
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Estandarizador"
        verbose_name_plural = "Estandarizadores"
