from django.db import models
from unittest.util import _MAX_LENGTH
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from componente.models import Componente
from ingrediente.models import Ingrediente
from usuarios.models import Usuario

# Create your models here.
class Receta (models.Model):
    codReceta=models.CharField(unique=True,max_length=50, verbose_name="Código Receta")
    nomReceta=models.CharField(max_length=50, verbose_name="Nombre Receta")
    class Estado(models.TextChoices):
      ACTIVO='1', _('Activo')
      INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    estandar=models.CharField(max_length=50, verbose_name="Estandar")
    preparacion=models.TextField(verbose_name="Preparación", null=True)
    codIngrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE, verbose_name="Código ingrediente", null=True, default=None)
  
    def __str__(self):
        fila = "Codigo: "+ self.codReceta + "Nombre: "+ self.nomReceta
        return fila
  
class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"



      

    