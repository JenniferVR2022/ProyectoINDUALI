from django.db import models
from enum import unique
from msilib.schema import Control
from tkinter import ACTIVE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Receta (models.Model):
    codReceta=models.CharField(max_length=50, verbose_name="Cod Receta")
    nomReceta=models.CharField(max_length=50, verbose_name="Nom Receta")
    class Estado(models.TextChoices):
          ACTIVO='True', _('Activo')
          INACTIVO='False', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    estandar=models.CharField(max_length=50, verbose_name="Estandar")
    consecutivo=models.CharField(max_length=50, verbose_name="Consecutivo")
    codComponente=models.ForeignKey(Componente, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Cod Componente")

