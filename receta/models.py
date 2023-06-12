from django.db import models
from unittest.util import _MAX_LENGTH
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from componente.models import Componente
from ingrediente.models import Ingrediente
from usuarios.models import Usuario

# Create your models here.
class Receta (models.Model):
    nomComponente = models.ForeignKey(Componente, on_delete=models.CASCADE, verbose_name="Nombre Componente", null=True, default=None)
    codReceta=models.CharField(unique=True,max_length=50, verbose_name="Código Receta")
    nomReceta=models.CharField(max_length=50, verbose_name="Nombre Receta")
    class Estado(models.TextChoices):
      ACTIVO='1', _('Activo')
      INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    estandar=models.CharField(max_length=50, verbose_name="Estandar")
    preparacion=models.TextField(verbose_name="Preparación", null=True)
    nomIngrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE, verbose_name="Nombre ingrediente", null=True, default=None)
    
    def __str__(self):
        fila = "Codigo: "+ self.codReceta + "Nombre: "+ self.nomReceta
        return fila
  
class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"
        
import csv
from django.db import transaction
from .models import Receta, Componente, Ingrediente

def importar_recetas_desde_csv(archivo_csv):
    with open(archivo_csv, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Ignorar la primera fila si contiene encabezados

        recetas = []
        for row in reader:
            cod_receta = row[0]
            nom_receta = row[1]
            estado = row[2]
            estandar = row[3]
            preparacion = row[4]

            # Obtener objetos Componente e Ingrediente relacionados
            nom_componente = row[5]
            componente = Componente.objects.get(nombre=nom_componente)

            nom_ingrediente = row[6]
            ingrediente = Ingrediente.objects.get(nombre=nom_ingrediente)

            receta = Receta(
                codReceta=cod_receta,
                nomReceta=nom_receta,
                estado=estado,
                estandar=estandar,
                preparacion=preparacion,
                nomComponente=componente,
                nomIngrediente=ingrediente,
            )
            recetas.append(receta)

    # Crear los objetos Receta en la base de datos en una transacción
    with transaction.atomic():
        Receta.objects.bulk_create(recetas)
