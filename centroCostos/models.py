from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

# Create your models here.
class CentroCosto(models.Model):
    codCentroCostos=models.CharField(max_length=50, verbose_name="Codigo Centro de Costos")
    nomCentroCostos=models.CharField(max_length=50, verbose_name="Nommbre Centro de Costos")
    nomEmpresa=models.CharField(max_length=50, verbose_name="Nombre Empresa")
    class Estado(models.TextChoices):
          ACTIVO='1', _('Activo')
          INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
