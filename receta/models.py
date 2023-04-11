from django.db import models
from unittest.util import _MAX_LENGTH
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from componente.models import Componente
from ingrediente.models import Ingrediente
from usuarios.models import Usuario

# Create your models here.
class Receta(models.Model):
    codReceta = models.CharField(max_length=50, verbose_name="Código Receta")
    nomReceta = models.CharField(max_length=50, verbose_name="Nombre Receta")
    
    class Estado(models.TextChoices):
        ACTIVO = 'True', 'Activo'
        INACTIVO = 'False', 'Inactivo'
        
    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    estandar = models.CharField(max_length=50, verbose_name="Estandar")
    preparacion = models.TextField(verbose_name="Preparación", null=True)
    codComponente = models.OneToOneField(Componente, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)

    def __str__(self):
        fila = "Codigo: " + self.codReceta + " Nombre: " + self.nomReceta
        return fila
  
  

# class RecetaDetalle(models.Model):
#       receta= models.ForeignKey(Receta, on_delete=models.CASCADE, verbose_name="Nombre Receta")
#       ingrediente= models.ForeignKey(Ingrediente, on_delete=models.CASCADE, verbose_name="Ingrediente") 

    