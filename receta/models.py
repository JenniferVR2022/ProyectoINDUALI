from django.db import models
from django.core.validators import MinValueValidator
from componente.models import Componente
from ingrediente.models import Ingrediente
from usuarios.models import Usuario

class Receta(models.Model):
    nomComponente = models.ForeignKey(Componente, on_delete=models.CASCADE, verbose_name="Nombre Componente", null=True, default=None)
    codReceta = models.CharField(unique=True, max_length=50, verbose_name="Código Receta")
    nomReceta = models.CharField(max_length=50, verbose_name="Nombre Receta")
    class Estado(models.TextChoices):
        ACTIVO = '1', 'Activo'
        INACTIVO = '0', 'Inactivo'
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    estandar = models.CharField(max_length=50, verbose_name="Estandar")
    preparacion = models.TextField(verbose_name="Preparación", null=True)
    nomIngrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE, verbose_name="Nombre ingrediente", null=True, default=None)
    
    # Nuevos campos
    cantidadMateriaPrima = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Cantidad de Materia Prima", default=0)
    costoTotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo Total", null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Cálculo del costo total
        if self.cantidadMateriaPrima and self.nomIngrediente:
            costo_ingrediente = float(self.nomIngrediente.costoIngrediente)
            self.costoTotal = (self.cantidadMateriaPrima * costo_ingrediente) / float(self.estandar)
        else:
            self.costoTotal = None
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Codigo: {self.codReceta}, Nombre: {self.nomReceta}"

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"
