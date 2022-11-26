from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from ingrediente.models import Ingrediente


class Ingrediente (models.Model):
    codIngrediente=models.CharField(max_length=50, verbose_name="Código Ingrediente")
    nomIngrediente=models.CharField(max_length=50, verbose_name="Nombre Ingrediente")
    unidadMedida=models.CharField(max_length=50, verbose_name="Unidad Medida")
    cantidadMateriaPrima=models.CharField(max_length=50, verbose_name="Cantidad Materia Prima")
    class Estado(models.TextChoices):
          ACTIVO='1', _('Activo')
          INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")