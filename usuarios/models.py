from enum import unique
from msilib.schema import Control
from tkinter import ACTIVE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Control (models.Model):
    fecha_creacion=models.DateField(verbose_name="Fecha de Creación", help_text=u"MM/DD/AAAA")






class Usuario (models.Model):
    
    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    apellido=models.CharField(max_length=50, verbose_name="Apellido")
    class TipoDocumento(models.TextChoices):
        CC='C.C', _('Cédula de Ciudadanía')
        CE='C.E', _('Cédula de Extranjería')
        PA='P.A', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="TipoDocumento")
    numeroDocumento=models.CharField(unique=True, max_length=50, verbose_name="Nùmero de documento")
    class tipoUsuario(models.TextChoices):
          Usuario='usuario', _('Usuario Estandar')
          Admin='admin', _('Administrador')
    tipoUsuario=models.CharField(max_length=20, choices=tipoUsuario.choices, default=tipoUsuario.Usuario, verbose_name="tipoUsuario")
    class Estado(models.TextChoices):
          ACTIVO='1', _('Activo')
          INACTIVO='0', _('Inactivo')
    Estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    correoElectronico=models.CharField(max_length=50, verbose_name="Correo electrónico")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    clave=models.CharField(max_length=20, verbose_name="Contraseña")
    control=models.ForeignKey(Control, on_delete=models.CASCADE, blank=False,null=True, verbose_name="IdUsuario") 