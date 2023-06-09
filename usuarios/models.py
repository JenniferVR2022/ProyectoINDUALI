
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

class Usuario (models.Model):
    nombres=models.CharField(max_length=50, verbose_name="Nombres")
    apellidos=models.CharField(max_length=50, verbose_name="Apellidos")
    email=models.CharField(max_length=50, verbose_name="Correo electrónico")
    
    class TipoDocumento(models.TextChoices):
        CC='C.C', _('Cédula de Ciudadanía')
        CE='C.E', _('Cédula de Extranjería')
        PA='P.A', _('Pasaporte')
    tipoDocumento=models.CharField(max_length=4,choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo Documento")
    documento=models.CharField(unique=True, max_length=50, verbose_name="Número Documento")
    
   
    class Rol(models.TextChoices):
        Administrador='Administrador', _('Administrador')
        Estandar='Estandar', _('Estandar')
        Invitado='Invitado', _('Invitado')
    rol=models.CharField(max_length=13,choices=Rol.choices, default=Rol.Invitado, verbose_name="Rol")
       
    class Estado(models.TextChoices):
          ACTIVO='1', _('Activo')
          INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    user=models.ForeignKey(User, on_delete= models.CASCADE)
   
   
    def __str__(self)->str:
        return "%s %s" %(self.nombres, self.apellidos)  