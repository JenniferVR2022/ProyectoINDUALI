from enum import unique
from msilib.schema import Control
from tkinter import ACTIVE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Usuario (models.Model):
    idUsuario=models.CharField(max_length=50, verbose_name="Id Usuario") 
    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    apellido=models.CharField(max_length=50, verbose_name="Apellido")
    
    class TipoDocumento(models.TextChoices):
        CC='C.C', _('Cédula de Ciudadanía')
        CE='C.E', _('Cédula de Extranjería')
        PA='P.A', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=20,choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo Documento")
    numeroDocumento=models.CharField(unique=True, max_length=50, verbose_name="Número Documento")
   
    class TipoUsuario(models.TextChoices):
          usuario='usuario', _('Usuario Estandar')
          admin='admin', _('Administrador')
    tipoUsuario=models.CharField(max_length=20,choices=TipoUsuario.choices, default=TipoUsuario.Usuario, verbose_name="Tipo Usuario")
   
    class Estado(models.TextChoices):
          ACTIVO='True', _('Activo')
          INACTIVO='False', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
    correoElectronico=models.CharField(max_length=50, verbose_name="Correo electrónico")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    clave=models.CharField(max_length=20, verbose_name="Contraseña")
    control=models.ForeignKey(Control, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Control")
 
class Componente (models.Model):
    CodComponente=models.BigIntegerField(max_length=50, verbose_name="Cod Componente")
    nomComponente=models.BigIntegerField(max_length=50, verbose_name="Nom Componente")

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

class CentroCostos (models.Model):
    codCentroCostos=models.CharField(max_length=50, verbose_name="Cod Centro Costos")
    nomCentroCostos=models.CharField(max_length=50, verbose_name="Nom Centro Costos")
    nomEmpresa=models.CharField(max_length=50, verbose_name="Nom Empresa")
    class Estado(models.TextChoices):
          ACTIVO='True', _('Activo')
          INACTIVO='False', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
class Control (models.Model):
    fecha_creacion=models.DateField(verbose_name="Fecha de Creación", help_text=u"MM/DD/AAAA")
    accion=models.CharField(max_length=50, verbose_name="Acción")
    idUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Id Usuario")
    idEstandarizador=models.ForeignKey(Estandarizador, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Id Estandarizador")
    
class Ingrediente (models.Model):
    codIngrediente=models.CharField(max_length=50, verbose_name="Cod Ingrediente")
    nomIngrediente=models.CharField(max_length=50, verbose_name="Nom Ingrediente")
    unidadMedida=models.CharField(max_length=50, verbose_name="Unidad Medida")
    cantidadMateriaPrima=models.CharField(max_length=50, verbose_name="Cantidad Materia Prima")
    
class ListaPrecio (models.Model):
    codListaPrecio=models.CharField(max_length=50, verbose_name="Cod Lista Precio")
    nomListaPrecio=models.CharField(max_length=50, verbose_name="Nom Lista Precio")
    tipoLista=models.CharField(max_length=50, verbose_name="Tipo Lista")
    
class Costos (models.Model):
    costoIngrediente=models.BigIntegerField(max_length=50, verbose_name="Costo Ingrediente")
    codIngrediente=models.ForeignKey(Ingrediente, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Cod Ingrediente")
    codListaPrecio=models.ForeignKey(ListaPrecio, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Cod Lista Precio")
    
class Estandarizador (models.Model):
    idEstandarizador=models.CharField(max_length=50, verbose_name="id Estandarizador")
    porcionesEstandar=models.CharField(max_length=50, verbose_name="Porciones Estandar")
    codCentroCostos=models.ForeignKey(CentroCostos, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Cod Centro Costos")
    codReceta=models.ForeignKey(Receta, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Cod Receta")
    codListaPrecio=models.ForeignKey(ListaPrecio, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Cod Lista Precio")
    codIngrediente=models.ForeignKey(Ingrediente, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Cod Ingrediente")  
