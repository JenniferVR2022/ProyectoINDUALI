from enum import unique
from msilib.schema import Control
from tkinter import ACTIVE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Usuario (models.Model):
    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    apellido=models.CharField(max_length=50, verbose_name="Apellido")
    class TipoDocumento(models.TextChoices):
        CC='C.C', _('Cédula de Ciudadanía')
        CE='C.E', _('Cédula de Extranjería')
        PA='P.A', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=20,choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo Documento")
    numeroDocumento=models.CharField(unique=True, max_length=50, verbose_name="Número Documento")
    class TipoUsuario(models.TextChoices):
          Usuario='usuario', _('Usuario Estandar')
          Admin='admin', _('Administrador')
    tipoUsuario=models.CharField(max_length=20,choices=TipoUsuario.choices, default=TipoUsuario.Usuario, verbose_name="Tipo Usuario")
    class Estado(models.TextChoices):
          ACTIVO='1', _('Activo')
          INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    correoElectronico=models.CharField(max_length=50, verbose_name="Correo electrónico")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    clave=models.CharField(max_length=20, verbose_name="Contraseña")