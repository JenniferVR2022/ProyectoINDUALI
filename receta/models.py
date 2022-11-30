from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from componente.models import Componente
from ingrediente.models import Ingrediente
from usuarios.models import Usuario


# from ingrediente.models import Ingrediente

# Create your models here.
class Receta (models.Model):
    codReceta=models.CharField(max_length=50, verbose_name="Código Receta")
    nomReceta=models.CharField(max_length=50, verbose_name="Nombre Receta")
    class Estado(models.TextChoices):
          ACTIVO='1', _('Activo')
          INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    estandar=models.CharField(max_length=50, verbose_name="Estandar")
    fkcodComponente=models.ForeignKey(Componente, on_delete=models.CASCADE, verbose_name="Código Componente")
    fkcodIngrediente=models.ForeignKey(Ingrediente, on_delete=models.CASCADE, verbose_name="Código Componente")
    super=models.ForeignKey(Usuario,verbose_name="Super",on_delete=models.CASCADE,related_name='Supervisor')
    def __str__(self):
        return self.codReceta

class RecetaDetalle(models.Model):
    receta= models.ForeignKey(Receta, on_delete=models.CASCADE, verbose_name="Nombre Receta")
    ingrediente= models.ForeignKey(Ingrediente, on_delete=models.CASCADE, verbose_name="Ingrediente") 

    