from django.db import models
from componente.models import Componente
from ingrediente.models import Ingrediente



class Receta(models.Model):
    nomComponente = models.ForeignKey(Componente, on_delete=models.CASCADE, verbose_name="Nombre Componente", related_name="recetas", null=True, default=None)
    codReceta = models.CharField(unique=True, max_length=50, verbose_name="Código Receta")
    nomReceta = models.CharField(max_length=50, verbose_name="Nombre Receta")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    estandar = models.CharField(max_length=50, verbose_name="Estandar")
    preparacion = models.TextField(verbose_name="Preparación", null=True)
    ingredientes = models.ManyToManyField(Ingrediente, through='RecetaIngrediente', verbose_name="Ingredientes", blank=True)
    # Nuevos campos

    def __str__(self):
        return f"Codigo: {self.codReceta}, Nombre: {self.nomReceta}"

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"



class RecetaIngrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Receta: {self.receta.nomReceta}, Ingrediente: {self.ingrediente.nomIngrediente}"

    class Meta:
        verbose_name = "Receta-Ingrediente"
        verbose_name_plural = "Recetas-Ingredientes"
