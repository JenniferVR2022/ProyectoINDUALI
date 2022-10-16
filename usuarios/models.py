from enum import unique
from msilib.schema import Control
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
        TI='T.I', _('Tarjeta de Identidad')
        OT='Otro', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numeroDocumento=models.CharField(unique=True, max_length=10, verbose_name="Numero de documento")
    tipoUsuario=models.CharField(max_length=30, verbose_name="Tipo de usuario")
    estado=models.CharField(max_length=50, verbose_name="Estado")
    correoElectronico=models.CharField(max_length=50, verbose_name="Correo electrónico")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    clave=models.CharField(max_length=50, verbose_name="Contraseña")
    
    class Rol(models.TextChoices):
        Administrador='Administrador', _('Administrador')
        Empleado='Empleado', _('Empleado')
       
    rol=models.CharField(max_length=13, choices=Rol.choices, default=Rol.Empleado, verbose_name="Rol")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
    