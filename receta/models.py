from django.db import models
from django.utils.translation import gettext_lazy as _
from componente.models import Componente
# from ingrediente.models import Ingrediente

# Create your models here.
class Receta (models.Model):
    codReceta=models.CharField(max_length=50, verbose_name="Cod Receta")
    nomReceta=models.CharField(max_length=50, verbose_name="Nom Receta")
    class Estado(models.TextChoices):
          ACTIVO='1', _('Activo')
          INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    estandar=models.CharField(max_length=50, verbose_name="Estandar")
    consecutivo=models.CharField(max_length=50, verbose_name="Consecutivo")
    fkcodComponente=models.ForeignKey(Componente, on_delete=models.CASCADE, verbose_name="Cod Componente")

# class RecetaDetalle(models.Model):
#       receta= models.ForeignKey(Receta, on_delete=models.CASCADE, verbose_name="Receta")
#       ingrediente= models.ForeignKey(Ingrediente, on_delete=models.CASCADE, verbose_name="Ingrediente")

    